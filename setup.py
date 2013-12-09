#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='watching_testrunner',
    description="Automatic test execution on file changes",
    long_description=open('README.rst').read(),
    url='https://github.com/tony/watching-testrunner',
    version='1.1.0',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: System :: Shells",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",

    ],
    author="Felix Schwarz, Martin Häcker, Robert Buchholz",
    author_email="felix.schwarz@web.de, spamfaenger@gmx.de, rbu@rbu.sh, "
                 "tony@git-pull.com",
    keywords="unit testing automation automatic test runner",
    py_modules=['watching_testrunner'],
    zip_safe=True,
    entry_points="""
         [console_scripts]
         watching_testrunner = watching_testrunner:main
     """,
)
