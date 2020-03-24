
from setuptools import setup, find_packages


setup(
    name="serverD",
    version="0.1.0",
    description="快速的服务器登录, 上传, 下载",
    long_description="快速的服务器登录, 上传, 下载",
    url="https://github.com/pansj66/serverD",
    author="shijiang Pan",
    author_email="1377161366@qq.com",
    license="MIT Licence",
    packages=find_packages(),
    #
    # packages=find_packages(include=[
    #     "serverD", "serverD.*",
    #     "serverE", "serverE.*",
    # ]),
    include_package_data=True,
    platforms=["all"],

    entry_points={
        'console_scripts': [
            "go = serverD.go:main",
            "get = serverD.go:get",
            "put = serverD.go:put",
        ]
    },

)
