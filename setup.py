import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name="serverD",
    version="0.1.0",
    description="快速的服务器登录, 上传, 下载",
    long_description="快速的服务器登录, 上传, 下载",
    url="pass",
    author="shijiang Pan",
    author_email="1377161366@qq.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Security",
        "Typing :: Typed",
    ],
    # packages=find_packages(include=[
    #     "mitmproxy", "mitmproxy.*",
    #     "pathod", "pathod.*",
    # ]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "go = serverD.go:main",
        ]
    },

)