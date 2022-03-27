"""
This is a setup.py script
"""
from setuptools import setup, find_packages
from glob import glob

VERSION = "0.1"
INSTALL = ["oss2", "notify2", "dbus-python", "PyQt5", "json"]
setup(
    name="PyQtPicUpload",
    version=VERSION,
    author="liyp",
    author_email="my@liyp.cc",
    description="a OSS Image Upload Tool",
    license="GPL3",

    url="https://git.liyp.cc/xmengnet/PyQtPicUpload",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX',
    ],

    platforms=["POSIX"],
    keywords=["IMAGE", "OSS"],
    install_requires=INSTALL,
    packages=find_packages(),
    # 安装过程中，需要安装的静态文件，如配置文件、service文件、图片等
    data_files=[
        ('resource', ['resource/current.qss']),
        ('image', ['images/up.png', 'images/upload.png', 'images/setting_icon.png', 'images/icon.svg'])
    ],
    include_package_data=True,
    # 用来支持自动生成脚本，安装后会自动生成 /usr/bin/foo 的可执行文件
    # 该文件入口指向 foo/main.py 的main 函数
    entry_points={
        'console_scripts': [
            'picupload = main.main:main'
        ]
    },
    python_requires=">=3.6",
)
