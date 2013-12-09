#!/usr/bin/env python
# -*- coding: utf8 -*-
import os, sys, platform
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='watching_testrunner',
    description="Automatic test execution on file changes",
    long_description=open('Readme.markdown').read(),
    url='http://häcker.net/trac/browser/open-source/python-watching-testrunner',
    version='1.0.1',
     # TODO: switch to hg versioning for ease of development
     # use_hg_version=True,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    author="Felix Schwarz, Martin Häcker, Robert Buchholz",
    author_email="felix.schwarz@web.de, spamfaenger@gmx.de, rbu@rbu.sh",
    # TODO: move main repo to bitbucket
    keywords="unit testing automation automatic test runner",
    
    py_modules=['watching_testrunner'],
    zip_safe=True,
    entry_points = """
         [console_scripts]
         watching_testrunner = watching_testrunner:main
     """,
 )