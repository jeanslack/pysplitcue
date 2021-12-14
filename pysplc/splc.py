"""
First release: 25/08/2012

Name: pysplitcue
Porpose: wraps the shnsplit and cuetag commands
Platform: Mac OsX, Gnu/Linux
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: Dec 13 2021
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
import shutil
import argparse
import subprocess
import tempfile
from pysplc.str_utils import information

# strings of information
INFO = information()
DATA = INFO[0]


def check_executables():
    """
    check for binaries: Returns the cuetag script
    (On Slackware 14.1 it is named cuetag.sh)
    """
    if which('cuetag'):
        cuetag = which('cuetag')
    elif which('cuetag.sh'):
        cuetag = which('cuetag.sh')
    else:
        sys.stderr.write("\033[31;1mERROR:\033[0m pysplitcue: 'cuetag' "
                         "is required, please install 'cuetools'.\n")
        sys.exit(1)

    if not which('shntool'):
        sys.stderr.write("\033[31;1mERROR:\033[0m pysplitcue: 'shntool' "
                         "is required, please install it.\n")
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


def run_process_splitting(filecue, audiofile, preferred_format, tmpdir):
    """
    Compare the dict keys to get the matched string value
    required by `shnsplit` command.
    """
    name = os.path.splitext(audiofile)[0]
    inputformat = os.path.splitext(audiofile)[1].replace('.', '', 1)

    cmd_split = {'wav:wav': (f'shnsplit -o wav -f "{filecue}" '
                             f'-t "%n - %t.split" -d "{tmpdir}" "{name}.wav"'),

                 'wav:flac': (f'shnsplit -o flac -f "{filecue}" '
                              f'-t "%n - %t" -d "{tmpdir}" "{name}.wav"'),

                 'wav:ape': (f'shnsplit -o ape -f "{filecue}" '
                             f'-t "%n - %t" -d "{tmpdir}" "{name}.wav"'),

                 'flac:wav': (f'shnsplit -o wav -f "{filecue}" '
                              f'-t "%n - %t" -d "{tmpdir}" "{name}.flac"'),

                 'flac:flac': (f'shnsplit -o flac -f "{filecue}" '
                               f'-t "%n - %t" -d "{tmpdir}" "{name}.flac"'),

                 'flac:ape': (f'shnsplit -o ape -f "{filecue}" '
                              f'-t "%n - %t" -d "{tmpdir}" "{name}.flac"'),

                 'ape:wav': (f'shnsplit -o wav -f "{filecue}" '
                             f'-t "%n - %t" -d "{tmpdir}" "{name}.ape"'),

                 'ape:flac': (f'shnsplit -o flac -f "{filecue}" '
                              f'-t "%n - %t" -d "{tmpdir}" "{name}.ape"'),

                 'ape:ape': (f'shnsplit -o ape -f "{filecue}" '
                             f'-t "%n - %t.split" -d "{tmpdir}" "{name}.ape"')
                 }

    if f'{inputformat}:{preferred_format}' in cmd_split:
        print("\nOn splitting audio tracks...")
        split = cmd_split[f'{inputformat}:{preferred_format}']
        try:
            subprocess.run(split, check=True, shell=True)

        except subprocess.CalledProcessError as err:
            sys.exit(f"\033[31;1mERROR:\033[0m {err}")

        else:
            print("\033[1m...done splitting\033[0m")
    else:
        msg = f"Unsupported input file format '{inputformat}'"
        sys.exit(f"\033[31;1mERROR:\033[0m {msg}")
# ----------------------------------------------------------#


def run_process_tagging(filename, audiofile, preferred_format):
    """
    Compare the dict keys to get the matched string value
    required by `cuetag` command.
    """
    exitstatus = None
    cuetag = check_executables()
    inputformat = os.path.splitext(audiofile)[1].replace('.', '', 1)

    cmd_tag = {'wav:flac': f'{cuetag} "{filename}" *.flac',
               'flac:flac': f'{cuetag} "{filename}" *.flac',
               'ape:flac': f'{cuetag} "{filename}" *.flac'}

    if f'{inputformat}:{preferred_format}' in cmd_tag:
        print("\nApply tags on audio tracks...")
        tag = cmd_tag[f'{inputformat}:{preferred_format}']

        try:
            subprocess.run(tag, check=True, shell=True)

        except subprocess.CalledProcessError as err:
            sys.exit(f"\033[31;1mERROR:\033[0m {err}")

        else:
            print("\033[1m...done tagging\033[0m")
    else:
        exitstatus = (f"Unsupported file format for "
                      f"tagging '{preferred_format}' ..skip")

    return exitstatus
# ----------------------------------------------------------#


def make_subdir(outputdir, tmpdir):
    """
    By giving the -o option, the user can supply a path
    with the name of a given folder for the output files.
    """
    if not outputdir == '.':
        try:
            os.mkdir(outputdir, mode=0o777)
        except OSError:
            print("\033[32;1mINFO:\033[0m A destination folder "
                  "already exists ..skip")

    for track in os.listdir(tmpdir):
        try:
            shutil.move(os.path.join(tmpdir, track),
                        os.path.join(outputdir, track))
        # Catching too general exception Exception (fixme)
        except Exception as err:
            sys.exit(f"\033[31;1mERROR:\033[0m {err}")
# ----------------------------------------------------------#


def cuefile_reading(fname, suffix):
    """
    Given a *.cue sheet file, it extracts the titles
    of the audio tracks to be split. Returns a tuple
    with the relative name of the audio file and a
    dictionary containing the names of the audio tracks .
    """
    num = 'TITLE'
    titletracks = {}

    with open(fname, 'r', encoding='utf8') as cue:
        filecue = cue.readlines()

    for line in filecue:
        if 'FILE' in line:
            titletracks['FILE'] = line.split('"')[1]

        if 'TRACK' in line:
            num = line.strip().split()[1]

        if 'TITLE' in line:
            title = line.split('"')[1]
            titletracks[num] = (f'{num} - {title}.{suffix}')

    return titletracks
# ----------------------------------------------------------#


def cuefile_check(filename):
    """
    Checks the CUE file. Returns True if error, None otherwise
    """
    error = None

    if not os.path.isfile(filename):
        error = True
    elif os.path.splitext(filename)[1] not in ('.cue', '.CUE'):
        error = True

    return error
# ----------------------------------------------------------#


def main():
    """
    Parser of the users inputs (evaluates positional arguments)
    using the argparser module.
    """
    parser = argparse.ArgumentParser(
                prog=DATA['prg_name'],
                description=DATA['short_decript'],
                # add_help=False,
                )
    parser.add_argument(
                '-v', '--version',
                help="Show the current version and exit",
                # action="store_true",
                action='version',
                version=f"pysplitcue v{DATA['version']} - {DATA['release']}",
                       )
    parser.add_argument(
                '-c', '--check-requires',
                help="List of installed or missing dependencies",
                action="store_true",
                required=False,
                       )
    parser.add_argument(
                '-p', '--preferred-format',
                choices=["wav", "flac", "ape"],
                help="Preferred audio format to output, default is flac",
                required=False,
                default='flac',
                        )
    parser.add_argument(
                '-i', '--input-cuefile',
                metavar='IMPUTFILE',
                # type=str,
                help=("INPUTFILE must be a CUE sheet with '.cue' "
                      "filename extension"),
                # dest='enable_config',
                # action='store_true',
                # nargs='?',
                # default=PWD,
                action="store",
                required=True,
                )
    parser.add_argument("-o", "--output-dir",
                        action="store",
                        type=str,
                        dest="outputdir",
                        help="Output directory, default '.'",
                        required=False,
                        default='.')

    args = parser.parse_args()

    if args.check_requires:
        dependencies()

    elif args.input_cuefile:
        filename = args.input_cuefile
        dirname = os.path.dirname(filename)
        fname = os.path.basename(filename)
        outputdir = args.outputdir
        suffix = args.preferred_format

        error = cuefile_check(filename)
        if error:
            parser.error(f"Invalid file: '{filename}'\n"
                         f"Provide a CUE sheet file (*.cue or *.CUE format).")
        else:
            os.chdir(dirname)
            titletracks = cuefile_reading(fname, suffix)
        if not titletracks:
            sys.exit(f"pysplitcue: error: Unable to read: '{filename}'")
        else:
            with tempfile.TemporaryDirectory(suffix=None,
                                             prefix='pysplitcue_',
                                             dir=None) as tmpdir:
                run_process_splitting(fname,
                                      titletracks['FILE'],
                                      suffix,
                                      tmpdir
                                      )
                os.chdir(tmpdir)
                runtag = run_process_tagging(filename,
                                             titletracks['FILE'],
                                             suffix
                                             )
                if runtag:
                    print(f"\033[33;1mWARNING:\033[0m {runtag}")

                os.chdir(dirname)
                make_subdir(outputdir, tmpdir)

            print("\033[1mFinished!\n\033[0m")
            sys.exit(0)


if __name__ == '__main__':
    main()
