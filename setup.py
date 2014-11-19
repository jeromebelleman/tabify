#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='tabify',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Tidy up tables",
    long_description="Tidy up tables, e.g. TWiki ones.",
    scripts=['tabify'],
    data_files=[('share/man/man1', ['tabify.1'])],
)
