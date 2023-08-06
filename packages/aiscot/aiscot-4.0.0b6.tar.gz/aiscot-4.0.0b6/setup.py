#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the AIS Cursor-On-Target Gateway.

Source:: https://github.com/ampledata/aiscot
"""

import os
import sys

import setuptools

__title__ = "aiscot"
__version__ = "4.0.0b6"
__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2022 Greg Albrecht"
__license__ = "Apache License, Version 2.0"


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == "publish":
        os.system("python setup.py sdist")
        os.system("twine upload dist/*")
        sys.exit()


publish()


def read_readme(readme_file="README.rst") -> str:
    """Read the contents of the README file for use as a long_description."""
    readme: str = ""
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, readme_file), encoding="utf-8") as frm:
        readme = frm.read()
    return readme


setuptools.setup(
    version=__version__,
    name=__title__,
    packages=[__title__],
    package_dir={__title__: __title__},
    url=f"https://github.com/ampledata/{__title__}",
    description="AIS Cursor-On-Target Gateway.",
    author="Greg Albrecht",
    author_email="oss@undef.net",
    package_data={"": ["LICENSE", "data/*"]},
    license="Apache License, Version 2.0",
    long_description=read_readme(),
    long_description_content_type="text/x-rst",
    zip_safe=False,
    include_package_data=True,
    install_requires=["pytak", "aiohttp"],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords=["Sailing", "AIS", "Cursor on Target", "ATAK", "TAK", "CoT"],
    entry_points={"console_scripts": ["aiscot = aiscot.commands:cli"]},
)
