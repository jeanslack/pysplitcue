"""
First release: 25/08/2012

Name: pysplitcue
Porpose: wraps the shnsplit and cuetag commands
Platform: Mac OsX, Gnu/Linux
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: January 26 2015, Nov 21 2017, Nov 24 2017, Aug 8 2018, Dec 06 2021
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
import sys
import os
from shutil import which
import argparse
import subprocess
from pysplc.str_utils import strings

# strings of information
cr = strings()
DATA = cr[0]


def check_essentials():
    """check the essentials """
    if which('cuetag'):
        cuetag = which('cuetag')
    elif which('cuetag.sh'):
        cuetag = which('cuetag')
    else:
        sys.stderr.write("pysplitcue: ERROR: cuetag is required, "
                         "please install 'cuetools'.\n")
        sys.exit(1)

    if not which('shntool'):
        sys.stderr.write("pysplitcue: ERROR: 'shntool' is required, "
                         "please install it.\n")
        sys.exit(1)

    return cuetag
# ----------------------------------------------------------#


def dependencies():
    """
    Check for dependencies

    """
    listing = ['flac', 'mac', 'wavpack', 'shntool', 'cuebreakpoints',
               'cueconvert', 'cueprint']
    for required in listing:
        # if which(required):
        if which(required, mode=os.F_OK | os.X_OK, path=None):

            print(f"Check for: '{required}' ..Ok")
        else:
            print(f"Check for: '{required}' ..Not Installed")

    if which('cuetag', mode=os.F_OK | os.X_OK, path=None):
        print("Check for: 'cuetag' ..Ok")

    elif which('cuetag.sh', mode=os.F_OK | os.X_OK, path=None):
        print("Check for: 'cuetag.sh' ..Ok")
    else:
        print("Check for: 'cuetag' ..Not Installed")
# ----------------------------------------------------------#


def run_process(in_ext, out_ext, name):
    """
    All final processes

    """
    cuetag = check_essentials()
    in_ext = in_ext.replace('.', '', 1)
    name = os.path.splitext(name)[0]

    cmd_split = {'wav:wav': (f'shnsplit -o wav -f "{name}.cue" '
                             f'-t "%n - %t.split" "{name}.wav"'),
                 'wav:flac': (f'shnsplit -o flac -f "{name}.cue" '
                              f'-t "%n - %t" "{name}.wav"'),
                 'wav:ape': (f'shnsplit -o ape -f "{name}.cue" '
                             f'-t "%n - %t" "{name}.wav"'),
                 'flac:wav': (f'shnsplit -o wav -f "{name}.cue" '
                              f'-t "%n - %t" "{name}.flac"'),
                 'flac:flac': (f'shnsplit -o flac -f "{name}.cue" '
                               f'-t "%n - %t" "{name}.flac"'),
                 'flac:ape': (f'shnsplit -o ape -f "{name}.cue" '
                              f'-t "%n - %t" "{name}.flac"'),
                 'ape:wav': (f'shnsplit -o wav -f "{name}.cue" '
                             f'-t "%n - %t" "{name}.ape"'),
                 'ape:flac': (f'shnsplit -o flac -f "{name}.cue" '
                              f'-t "%n - %t" "{name}.ape"'),
                 'ape:ape': (f'shnsplit -o ape -f "{name}.cue" '
                             f'-t "%n - %t.split" "{name}.ape"')
                 }

    if f'{in_ext}:{out_ext}' in cmd_split:
        # print(cmd_split[f'{in_ext}:{out_ext}'])#print command for debug
        split = cmd_split[f'{in_ext}:{out_ext}']
        try:
            subprocess.check_call(split, shell=True)
            print("\033[1m...done.\033[0m")

        except subprocess.CalledProcessError as err:
            sys.exit(f"\033[31;1mProcess Error!\033[0m {err}")

        cmd_tag = {'wav:flac': f'{cuetag} "{name}.cue" *.flac',
                   'flac:flac': f'{cuetag} "{name}.cue" *.flac',
                   'ape:flac': f'{cuetag} "{name}.cue" *.flac'
                   }

        if f'{in_ext}:{out_ext}' in cmd_tag:
            print("\nApply tags on audio tracks...\n")
            try:
                tag = cmd_tag[f'{in_ext}:{out_ext}']
                subprocess.check_call(tag, shell=True)
                print("\033[1m...done.\033[0m")

            except subprocess.CalledProcessError as err:
                sys.exit(f"\033[31;1mProcess Error!\033[0m {err}")
# ----------------------------------------------------------#


def checker(out_ext, filename):
    """
    file check utility, evaluates if the file exists,
    if the audio format is supported and also evaluates
    whether the corresponding .cue file
    """
    filename = os.path.abspath(filename)
    format_list = ['.wav', '.flac', '.ape']
    cuelist = []
    name = os.path.basename(filename)
    in_ext = os.path.splitext(name)

    if os.path.isfile(filename):
        os.chdir(os.path.dirname(filename))
        for fname in os.listdir():
            if os.path.splitext(fname)[1] in '.cue':
                cuelist.append(fname)

        if not in_ext[1] in format_list:
            sys.exit(f"pysplitcue: error: unrecognized input format "
                     f"'{in_ext[1]}', choose between  {format_list}")

        if f'{in_ext[0]}.cue' in cuelist:
            run_process(in_ext[1], out_ext, name)
        else:
            sys.exit(f"pysplitcue: error: No such CUE sheet file"
                     f"named: '{in_ext[0]}.cue'")
    else:
        sys.exit(f"pysplitcue: error: No such file: '{filename}'")
# ----------------------------------------------------------#


def main():
    """
    Parser of the users inputs (evaluates positional arguments)
    """
    parser = argparse.ArgumentParser(
                description=DATA['short_decript'],)
    parser.add_argument(
                '-v', '--version',
                help="show the current version and exit",
                action="store_true",
                       )
    parser.add_argument(
                '-c', '--check',
                help="list of installed or missing dependencies",
                action="store_true",
                       )
    parser.add_argument(
                '-o',
                choices=["wav", "flac", "ape"],
                help="output audio format"
                        )
    parser.add_argument(
                '-i',
                metavar='FILE',
                # type=str,
                help="input audio filename to splitting",
                # dest='enable_config',
                # action='store_true',
                # nargs='?',
                # default=PWD,
                # action="store_true"
                       )

    args = parser.parse_args()

    if args.check:
        dependencies()
    elif args.o:
        if not args.i:
            sys.exit('pysplitcue: error: missing option -i ..FILE')
        checker(args.o, args.i)
    elif args.version:
        print(f"pysplitcue v{DATA['version']} - {DATA['release']}")
        return
    else:
        print("Type 'pysplitcue -h' for help.")
