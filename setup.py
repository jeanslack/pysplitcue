#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# First release: Monday, July 7 10:00:47 2014
# 
#########################################################
# Name: setup.py
# Porpose: building pysplitcue sources and package
# USAGE: python3 setup.py sdist bdist_wheel
# Platform: Gnu/Linux-Unix-MacOs
# Writer: jeanslack <jeanlucperni@gmail.com>
# license: GPL3
# Rev: Sept 24 2014, Jan 26 2015, Nov 22 2017, Aug 8 2019
#########################################################

# ---- Imports ----#
from distutils.core import setup
from setuptools import setup, find_packages
from glob import glob
import sys
import os
from pysplc.str_utils import strings

cr = strings()
AUTHOR = cr[0]
MAIL = cr[1]
COPYRIGHT = cr[2]
VERSION = cr[3]
RELEASE = cr[4]
RLS_NAME = cr[5]# release name first letter is Uppercase
PRG_NAME = cr[6]
URL = cr[7]
BLOGSPOT = cr[8]
DESCRIPTION = cr[9]
LONG_DESCRIPTION = cr[10]
LONG_HELP = cr[11]
SHORT_HELP = cr[12]
LICENSE = cr[14]# short_license

# ---- categorize with ----#
CLASSIFIERS = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Multimedia :: Sound/Audio :: Conversion',
            'Topic :: Utilities',
                ]

#----------  Source/Build distributions  ----------------#

# get the package data
DATA_FILES = [('share/man/man1', ['man/pysplitcue.1.gz']),
                ('share/pysplitcue', ['AUTHORS', 'BUGS',
                                    'CHANGELOG', 'COPYING', 
                                    'TODO', 'README.md']),
                ]
setup(name=PRG_NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=MAIL,
        url=URL,
        license=LICENSE,
        platforms=["Linux","Unix","MacOS"],
        packages=find_packages(),
        scripts=['pysplitcue'],
        data_files=DATA_FILES,
        classifiers=CLASSIFIERS,
        #install_requires=REQUIRES,
        )
