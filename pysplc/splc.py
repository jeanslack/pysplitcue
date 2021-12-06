"""
First release: 25/08/2012

Name: pysplitcue
Porpose: wraps the shnsplit and cuetag commands
Platform: Mac OsX, Gnu/Linux
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: January 26 2015, Nov 21 2017, Nov 24 2017, Aug 8 2018, Dec 06 2021
Code checker: flake8 and pylint
"""

import sys
import os
from shutil import which
import argparse
import subprocess
from pysplc.str_utils import strings

# strings of information
cr = strings()
PRG_NAME = cr[6]
VERSION = cr[3]
RELEASE = cr[4]
WEBPAGE = cr[7]
BLOGSPOT = cr[8]
LONG_HELP = cr[11]
SHORT_HELP = cr[12]
TRY_HELP = cr[15]


def check_essentials():
    """check the essentials """
    if which('cuetag'):
        cuetag = which('cuetag')
    elif which('cuetag.sh'):
        cuetag = which('cuetag')
    else:
        sys.stderr.write("pysplitcue:ERROR: cuetag is required, "
                         "please install 'cuetools'.\n")
        sys.exit(1)
    if not which('shntool'):
        sys.stderr.write("pysplitcue:ERROR: 'shntool' is required, "
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

    split_dict = {'wav:wav': (f'shnsplit -o wav -f "{name}.cue" '
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

    tag_dict = {'wav:flac': f'{cuetag} "{name}.cue" *.flac',
                'flac:flac': f'{cuetag} "{name}.cue" *.flac',
                'ape:flac': f'{cuetag} "{name}.cue" *.flac'
                }

    if f'{in_ext}:{out_ext}' in split_dict:
        # print(split_dict[f'{in_ext}:{out_ext}'])#print command for debug
        try:
            command = split_dict[f'{in_ext}:{out_ext}']
            subprocess.check_call(command, shell=True)
            # makedir_move(".split.wav","Formato-wav")
            print("\033[1m...done.\033[0m")

        except subprocess.CalledProcessError as err:
            sys.exit(f"\033[31;1mProcess Error!\033[0m {err}")

        if f'{in_ext}:{out_ext}' in tag_dict:
            print("\nApply tags on audio tracks...\n")
            try:
                command = tag_dict[f'{in_ext}:{out_ext}']
                subprocess.check_call(command, shell=True)
                # makedir_move(".split.wav","Formato-wav")
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
    Parser of the users inputs (positional/optional arguments)
    """
    parser = argparse.ArgumentParser(
                description='Audio files cue splitting utility',)
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
        print(f'{VERSION} - {RELEASE}')
        return
    else:
        print("Type 'pysplitcue -h' for help.")
