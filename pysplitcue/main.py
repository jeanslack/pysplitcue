"""
First release: 25/08/2012

Name: main.py
Porpose: provides an argparser interface for PySplitCue class
Platform: MacOs, Gnu/Linux, FreeBSD
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: January 05 2022
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
import os
from shutil import which
import argparse

from pysplitcue.datastrings import informations
from pysplitcue.splitcue import PySplitCue
from pysplitcue.str_utils import msgcolor, msgdebug

from pysplitcue.exceptions import InvalidFile, ParserError, TempProcessError

# data strings
INFO = informations()
DATA = INFO[0]


def dependencies():
    """
    Check for dependencies
    """
    listtools = ('shntool', 'cuetag', 'cuetag.sh')
    listencoders = ('flac', 'mac', 'wavpack', 'lame', 'oggenc')

    print('--------------------------------')
    msgcolor(green="Required tools:")
    for required in listtools:
        if which(required, mode=os.F_OK | os.X_OK, path=None):
            msgcolor(head=f"Check for: '{required}'", azure="..Ok")
        else:
            msgcolor(head=f"Check for: '{required}'", orange="..Not Installed")
    print('--------------------------------')
    msgcolor(green="Available encoders:")
    for required in listencoders:
        if which(required, mode=os.F_OK | os.X_OK, path=None):
            msgcolor(head=f"Check for: '{required}'", azure="..Ok")
        else:
            msgcolor(head=f"Check for: '{required}'", orange="..Not Installed")
    print('--------------------------------')
# ----------------------------------------------------------#


def main():
    """
    Defines and evaluates positional arguments
    using the argparser module.
    """
    parser = argparse.ArgumentParser(prog=DATA['prg_name'],
                                     description=DATA['short_decript'],
                                     # add_help=False,
                                     )
    parser.add_argument('--version',
                        help="Show the current version and exit",
                        action='version',
                        version=(f"pysplitcue v{DATA['version']} "
                                 f"- {DATA['release']}"),
                        )
    parser.add_argument('-i', '--input-cuefile',
                        metavar='IMPUTFILE',
                        help=("An absolute or relative CUE sheet file, "
                              "i.e. with `.cue` extension"),
                        action="store",
                        required=True,
                        )
    parser.add_argument('-f', '--format-type',
                        choices=["wav", "wv", "flac", "ape", "mp3", "ogg"],
                        help=("Preferred audio format to output, "
                              "default is 'flac'"),
                        required=False,
                        default='flac',
                        )
    parser.add_argument("-o", "--output-dir",
                        action="store",
                        type=str,
                        dest="outputdir",
                        help=("Absolute or relative destination path for "
                              "output files. If a specified destination "
                              "folder does not exist, it will be created "
                              "automatically. By default it is the same "
                              "location as IMPUTFILE"),
                        required=False,
                        default='.')

    parser.add_argument("-ow", "--overwrite",
                        choices=["ask", "never", "always"],
                        dest="overwrite",
                        help=("Overwrite files on destination if they exist, "
                              "Default is `ask` before proceeding"),
                        required=False,
                        default='ask')
    parser.add_argument('-c', '--check-requires',
                        help="List of installed or missing dependencies",
                        action="store_true",
                        required=False,
                        )

    args = parser.parse_args()

    if args.check_requires:
        dependencies()

    elif args.input_cuefile:
        kwargs = {'filename': args.input_cuefile}
        kwargs['outputdir'] = args.outputdir
        kwargs['suffix'] = args.format_type
        kwargs['overwrite'] = args.overwrite

        try:
            split = PySplitCue(**kwargs)
            split.open_cuefile()
            split.do_operations()
            split.cuefile.close()
        except (InvalidFile,
                ParserError,
                TempProcessError) as error:
            msgdebug(err=f"{error}")


if __name__ == '__main__':
    main()
