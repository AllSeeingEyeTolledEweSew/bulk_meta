#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages

with open("README") as readme:
    documentation = readme.read()

setup(
    name="bulk_meta",
    version="0.0.1",
    description="Private tracker bulk metadata downloader",
    long_description=documentation,
    author="AllSeeingEyeTolledEweSew",
    author_email="allseeingeyetolledewesew@protonmail.com",
    url="http://github.com/AllSeeingEyeTolledEweSew/bulk_meta",
    license="Unlicense",
    packages=find_packages(),
    use_2to3=True,
    install_requires=[
        "btn>=0.1.2",
        "deluge_client_sync>=0.1.0",
        "better_bencode>=0.2.1",
    ],
    entry_points={
        "console_scripts": [
            "btn_bulk_meta = bulk_meta.btn:main",
        ],
    },
)
