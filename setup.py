#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
First release: Monday, July 7 10:00:47 2014

Name: setup.py
Porpose: building pysplitcue sources and package
USAGE: python3 setup.py sdist bdist_wheel
Platform: Gnu/Linux-Unix-MacOs
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: Sept 24 2014, Jan 26 2015, Nov 22 2017, Aug 8 2019, Dec 07 2021
Code checker: flake8, pylint
####################################################################

This file is part of pysplitcue.

    pysplitcue is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pysplitcue is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pysplitcue.  If not, see <http://www.gnu.org/licenses/>.

"""
from setuptools import setup, find_packages
from pysplitcue.str_utils import informations

cr = informations()
DATA = cr[0]
LONG_DESCRIPTION = cr[1]
LONG_HELP = cr[2]
SHORT_HELP = cr[3]
LICENSE = cr[6]  # short_license

CLASSIFIERS = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Topic :: Multimedia :: Sound/Audio :: Conversion',
            'Topic :: Utilities',
                ]

# get the package data
DATA_FILES = [('share/man/man1', ['man/pysplitcue.1.gz']),
              ('share/pysplitcue', ['AUTHORS', 'BUGS',
                                    'CHANGELOG', 'COPYING',
                                    'TODO', 'README.md']),
              ]

with open('README.md', 'r', encoding='utf8') as readme:
    long_descript = readme.read()

setup(name=DATA['prg_name'],
      version=DATA['version'],
      description=DATA['short_decript'],
      long_description=long_descript,
      long_description_content_type='text/markdown',
      author=DATA['author'],
      author_email=DATA['mail'],
      url=DATA['webpage'],
      license=LICENSE,
      platforms=["Linux", "Unix", "MacOS"],
      packages=find_packages(),
      data_files=DATA_FILES,
      zip_safe=False,
      python_requires=">=3.6",
      entry_points={
          "console_scripts": ['pysplitcue = pysplitcue.splitcue:main']},
      classifiers=CLASSIFIERS,
      )
