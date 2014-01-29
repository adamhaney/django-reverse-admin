#!/usr/bin/env python

import os
from setuptools import setup, find_packages

DESCRIPTION = "A django admin addon that allows ininlining reverse relationships"

def read(fname):
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...

    Wrapping this in a try block because it appears that IOErrors are being throw due to README.md not making its way to pypi
    """
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return DESCRIPTION

setup(
    name="django-reverse-admin",
    version="0.1.0",
    author="Adam Haney",
    author_email="adam.haney@campusbellhops.com",
    description=DESCRIPTION,
    license="LGPL",
    keywords="Django, admin",
    url="",
    packages=['reverseadmin'],
    long_description=read('README.md'),
    dependency_links = [],
    install_requires=[
        'django'
        ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        ],
)
