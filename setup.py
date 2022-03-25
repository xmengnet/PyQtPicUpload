"""
This is a setup.py script
"""
from setuptools import setup, find_packages

VERSION = "0.1"
INSTALL = ["oss2", "notify2", "dbus-python", "PyQt5", "json"]
PACKAGES = find_packages()

setup(
    name="PyQtPicUpload",
    version=VERSION,
    author="liyp",
    author_email="my@liyp.cc",
    description="a OSS Image Upload Tool",
    license="GPL3",
    include_package_data=True,
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
    keywords=["IMAGE","OSS"],
    exclude_package_date={'test':['']},
    install_requires=INSTALL,
    packages=PACKAGES,
    python_requires=">=3.6",
)