from setuptools import setup

setup(
    name="GUI",
    description="My Python GUI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xiaoyou009/GUI",
    author="Alex You",
    version="1.0.1",
    author_email="xiaoyou.hku@gmail.com",
    license="GPL-3.0-or-later",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.7",
    ],
    py_modules=["layout"],
)
