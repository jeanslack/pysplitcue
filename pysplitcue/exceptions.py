"""
Name: exceptions.py
Porpose: defines class Exceptions for pysplitcue
Platform: MacOs, Gnu/Linux, FreeBSD
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: January 04 2022
Code checker: flake8 and pylint
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


class InvalidFile(Exception):
    """Exception type raised when CUE file is invalid."""


class ParserError(Exception):
    """Exception type raised when a CUE file parser error occurs."""


class TempProcessError(Exception):
    """Exception raised while working in temp folder."""
