"""
First release: 25/08/2012

Name: splitcue.py
Porpose: wraps the shnsplit and cuetag commands
Platform: Mac OsX, Gnu/Linux
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: Dec 25 2021
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
from pysplitcue.str_utils import informations
from pysplitcue.datastrings import msgdebug, msgcolor, msgend

# strings of information
INFO = informations()
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
        msgdebug(err="'cuetag' is required, please install 'cuetools'.")
        sys.exit(1)

    if not which('shntool'):
        msgdebug(err="'shntool' is required, please install it.")
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

            msgcolor(head=f"Check for: '{required}'", azure="..Ok")
        else:
            msgcolor(head=f"Check for: '{required}'", orange="..Not Installed")

    if which('cuetag', mode=os.F_OK | os.X_OK, path=None):
        msgcolor(head="Check for: 'cuetag'", azure="..Ok")

    elif which('cuetag.sh', mode=os.F_OK | os.X_OK, path=None):
        msgcolor(head="Check for: 'cuetag.sh'", azure="..Ok")
    else:
        msgcolor(head="Check for: 'cuetag'", orange="..Not Installed")
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
        msgdebug(info="splitting audio tracks...")
        split = cmd_split[f'{inputformat}:{preferred_format}']
        try:
            subprocess.run(split, check=True, shell=True)

        except subprocess.CalledProcessError as err:
            msgdebug(err=f"{err}")
            sys.exit(1)

        else:
            msgdebug(info="...done splitting")
    else:
        msgdebug(err=f"Unsupported input file format '{inputformat}'")
        sys.exit(1)
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
        msgdebug(info="Apply tags on audio tracks...")
        tag = cmd_tag[f'{inputformat}:{preferred_format}']

        try:
            subprocess.run(tag, check=True, shell=True)

        except subprocess.CalledProcessError as err:
            msgdebug(err=f"{err}")
            sys.exit(1)

        else:
            msgdebug(info="...done tagging")
    else:
        exitstatus = (f"Unsupported file format for "
                      f"tagging '{preferred_format}' ..skip")

    return exitstatus
# ----------------------------------------------------------#


def make_subdir(outputdir):
    """
    By giving the -o option, the user can supply a path
    with the name of a given folder for the output files.
    """
    error = None
    if not outputdir == '.':
        try:
            os.mkdir(outputdir, mode=0o777)
        except OSError:
            msgdebug(warn="A destination folder already exists ..skip")
        except Exception as err:
            # Catching too general exception Exception (FIXME)
            error = err

    return error
# ----------------------------------------------------------#


def move_files_on_outputdir(outputdir, tmpdir, overwrite):
    """
    All files are processed in a /temp folder. After the split
    operation is complete, all tracks are moved from /temp folder
    to output folder. Here evaluates what to do if files already
    exists on output folder.

    """
    for track in os.listdir(tmpdir):
        if os.path.exists(track):
            if overwrite in ('n', 'N', 'y', 'Y', 'ask'):
                while True:
                    msgdebug(warn=f"File already exists: "
                             f"'{os.path.join(outputdir, track)}'\n")
                    overwrite = input("Overwrite [Y/n/all]? > ")
                    if overwrite in ('Y', 'y', 'n', 'N', 'all', 'ALL'):
                        break
                    msgdebug(err=f"Invalid option '{overwrite}'")
                    continue
            elif overwrite == 'never':
                msgdebug(warn=("Do not overwrite any files because "
                               "you specified '-w never' option"))
                return

        if overwrite in ('y', 'Y', 'all', 'ALL', 'always', 'never'):
            try:
                shutil.move(os.path.join(tmpdir, track),
                            os.path.join(outputdir, track))
            # Catching too general exception Exception (FIXME)
            except Exception as err:
                msgdebug(err=f"{err}")
                sys.exit(1)
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
                        help=("INPUTFILE must be a CUE sheet with '.cue' "
                              "filename extension"),
                        action="store",
                        required=True,
                        )
    parser.add_argument('-f', '--format-type',
                        choices=["wav", "flac", "ape"],
                        help=("Preferred audio format to output, "
                              "default is 'flac'"),
                        required=False,
                        default='flac',
                        )
    parser.add_argument("-o", "--output-dir",
                        action="store",
                        type=str,
                        dest="outputdir",
                        help="Output directory, default '.'",
                        required=False,
                        default='.')

    parser.add_argument("-ow", "--overwrite",
                        choices=["ask", "never", "always"],
                        dest="overwrite",
                        help=("Overwrite files on destination if they exist, "
                              "default is 'ask'"),
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
        filename = args.input_cuefile
        dirname = os.path.dirname(filename)
        fname = os.path.basename(filename)
        outputdir = args.outputdir
        suffix = args.format_type
        overwrite = args.overwrite

        error = cuefile_check(filename)
        if error:
            parser.error(f"Invalid file: '{filename}'\n"
                         f"Provide a CUE sheet file (*.cue or *.CUE format).")
        else:
            os.chdir(dirname)
            titletracks = cuefile_reading(fname, suffix)
        if not titletracks:
            msgdebug(err=f"pysplitcue: error: Unable to read: '{filename}'")
            sys.exit(1)
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
                    msgdebug(warn=f"{runtag}")

                os.chdir(dirname)
                msbdir = make_subdir(outputdir)
                if msbdir is not None:
                    msgdebug(err=f"{msbdir}")
                    msgend(abort=True)
                    sys.exit(1)

                move_files_on_outputdir(outputdir, tmpdir, overwrite)
                msgend(done=True)
                sys.exit(0)


if __name__ == '__main__':
    main()
