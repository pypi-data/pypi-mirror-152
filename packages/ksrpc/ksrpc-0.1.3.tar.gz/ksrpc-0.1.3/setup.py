import setuptools

with open("README.md", "r", encoding='utf-8') as fp:
    long_description = fp.read()

version = {}
with open("ksrpc/_version.py", encoding="utf-8") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="ksrpc",
    version=version['__version__'],
    author="wukan",
    author_email="wu-kan@163.com",
    description="Keep Simple RPC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wukan1986/ksrpc",
    packages=setuptools.find_packages(),
    install_requires=[
        'httpx',
        'loguru',
        'nest-asyncio',
        'pandas',
        'requests',
        'websockets',
    ],
    extras_require={
        'server': [
            'aioredis',
            'fakeredis',
            'fastapi',
            'python-multipart',
            'uvicorn[standard]',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    python_requires=">=3.7",
)
