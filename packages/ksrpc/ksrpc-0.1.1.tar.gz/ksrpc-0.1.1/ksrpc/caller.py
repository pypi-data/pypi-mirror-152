#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author     :wukan
# @License    :(C) Copyright 2022, wukan
# @Date       :2022-05-09
"""
调用器
根据指定参数，调用，并返回结果
"""

import hashlib
import inspect
from datetime import datetime

from fastapi import status
from loguru import logger

from .cache import async_cache_get, async_cache_setex
from .config import (
    METHODS_CHECK, METHODS_ALLOW, METHODS_BLOCK, IP_CHECK,
)
from .model import RspModel
from .serializer.pkl_gzip import serialize
from .utils.async_ import to_async
from .utils.ip_ import in_whitelist


def check_methods(dict_, list_, default):
    """方法权限检查"""
    d = dict_
    for x in list_:
        d = d.get(x, default)
        if isinstance(d, bool):
            return d
    return d


def make_key(func, args, kwargs):
    args_kwargs = f'{repr(args)}_{repr(kwargs)}'
    if len(args_kwargs) > 32:
        args_kwargs = hashlib.md5(args_kwargs.encode('utf-8')).hexdigest()
    return f'{func}_{args_kwargs}'


async def call(host, user, func, args, kwargs, cache_get, cache_expire):
    try:
        if IP_CHECK:
            if not in_whitelist(host):
                raise Exception(f"{host} blocked. Copyright protection, Intranet use only")

        if user is None:
            raise Exception(f"Unauthorized")

        methods = func.split('.')
        module = methods[0]

        if METHODS_CHECK:
            if not check_methods(METHODS_ALLOW, methods, False):
                raise Exception(f'Method Not Allowed, {func} not in allowlist')
            if not check_methods(METHODS_BLOCK, methods, True):
                raise Exception(f'Method Not Allowed, {func} in blocklist')

        buf = None
        data = None  # None表示从缓存中取的，需要其它格式时需要转换
        # cache所用的key
        key = make_key(func, args, kwargs)

        if cache_get:
            # 优先取缓存
            buf = await async_cache_get(key)
        if buf is None:
            cache_expire, buf, data = await _call(func, module, methods[1:], args, kwargs, cache_expire)
            # 过短的缓存时间没有必要
            if cache_expire >= 30:
                # 就算强行去查询数据，也会想办法存下，再次取时还能从缓存中取
                await async_cache_setex(key, cache_expire, buf)
                logger.info(f'To cache: expire:{cache_expire}\tlen:{len(buf)}\t{key}')
        else:
            logger.info(f'From cache: {func}\t{args}\t{kwargs}')

    except Exception as e:
        key = type(e).__name__
        # 这里没有缓存，因为这个错误是服务器内部检查
        data = RspModel(status=status.HTTP_403_FORBIDDEN,
                        datetime=datetime.now().isoformat(),
                        func=func,
                        args=args,
                        kwargs=kwargs)
        data.type = type(e).__name__
        data.data = repr(e)
        data = data.dict()
        buf = serialize(data).read()

    return key, buf, data


async def _call(func_name, module, methods, args, kwargs, cache_expire):
    try:
        # 当前server目录下文件，用于特别处理
        api = __import__(f'{__package__}.server.{module}', fromlist=['*'])
    except ModuleNotFoundError as e:
        # 导入系统包
        api = __import__(module, fromlist=['*'])

    # 返回的数据包
    d = RspModel(status=status.HTTP_200_OK,
                 datetime=datetime.now().isoformat(),  # 加查询时间，缓存中也许可以判断是否过期
                 func=func_name,
                 args=args,
                 kwargs=kwargs)

    try:
        # 转成字符串，后面可能于做cache的key
        logger.info(f'Call: {func_name}\t{args}\t{kwargs}')

        func = api
        for method in methods:
            func = getattr(func, method)

        # 可以调用的属性
        if callable(func):
            # 例如os.remove
            type_ = 'function'
            if not inspect.iscoroutinefunction(func):
                # 阻塞了会影响后面的请求处理，请求其实已经收到在队列中, 所以转成异步
                func = to_async(func)
            # 全当成异步使用
            func = await func(*args, **kwargs)

        # 结果的类型名
        class_name = func.__class__.__name__

        # 不可调用的直接返回
        if class_name == 'module':
            # 例如os.path，但用法为os.path()
            data = repr(func)
            cache_expire = 0
        elif class_name in ('dict_keys', 'dict_values'):
            # 无法序列化，只能强行转换
            # 例如：sys.modules.keys(), 也可以sys.modules.keys.__list()
            data = list(func)
            cache_expire = 0
        else:
            # 例如math.pi，但用法math.pi()
            data = func

        d.type = type(func).__name__
        d.data = data

        # pkl序列化，为了能完整还源
        d = d.dict()
        buf = serialize(d).read()

    except Exception as e:
        d.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        d.type = type(e).__name__
        d.data = repr(e)
        # 错误也缓存一会，防止用户写了死循环搞崩上游
        cache_expire = 60
        d = d.dict()
        buf = serialize(d).read()

    return cache_expire, buf, d
