"""
First release: 25/08/2012

Name: splitcue.py
Porpose: wraps the shnsplit and cuetag commands
Platform: Mac OsX, Gnu/Linux
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: Dec 29 2021
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
    run `shnsplit` command. Returns string error if
    error, None otherwise.
    """
    if not which('shntool'):
        return "'shntool' is required, please install it."

    name = os.path.splitext(audiofile)[0]
    cmd_split = (f'shnsplit -o {preferred_format} -f "{filecue}" '
                 f'-t "%n - %t" -d "{tmpdir}" "{name}.{preferred_format}"')

    msgdebug(info="splitting audio tracks...")
    try:
        subprocess.run(cmd_split, check=True, shell=True)

    except subprocess.CalledProcessError as err:
        msgdebug(err=f"{err}")
        return err

    else:
        msgdebug(info="...done splitting")

    return None
# ----------------------------------------------------------#


def run_process_tagging(filename, preferred_format):
    """
    run `cuetag` command. Returns string error if
    error, None otherwise.
    """
    if which('cuetag'):
        cuetag = which('cuetag')
    elif which('cuetag.sh'):
        cuetag = which('cuetag.sh')
    else:
        return "'cuetag' is required, please install 'cuetools'."

    if preferred_format == 'flac':
        msgdebug(info="Apply tags on audio tracks...")
        cmd_tag = f'{cuetag} "{filename}" *.flac'

        try:
            subprocess.run(cmd_tag, check=True, shell=True)

        except subprocess.CalledProcessError as err:
            return err

        else:
            msgdebug(info="...done tagging")
    else:
        msgdebug(warn=(f"Unsupported file format '{preferred_format}' "
                       f"for tagging  ..skip"))

    return None
# ----------------------------------------------------------#


def make_subdir(outputdir):
    """
    By giving the -o option, the user can supply a custom
    folder for the output files. Returns string error if
    error, None otherwise.

    """
    error = None
    if not outputdir == '.':
        try:
            os.makedirs(os.path.abspath(outputdir), mode=0o777)
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
    Returns string error if error, None otherwise.

    """
    outputdir = os.path.abspath(outputdir)
    for track in os.listdir(tmpdir):
        if os.path.exists(os.path.join(outputdir, track)):
            if overwrite in ('n', 'N', 'y', 'Y', 'ask'):
                while True:
                    msgdebug(warn=f"File already exists: "
                             f"'{os.path.join(outputdir, track)}'")
                    overwrite = input("Overwrite [Y/n/all]? > ")
                    if overwrite in ('Y', 'y', 'n', 'N', 'all', 'ALL'):
                        break
                    msgdebug(err=f"Invalid option '{overwrite}'")
                    continue
            elif overwrite == 'never':
                msgdebug(warn=("Do not overwrite any files because "
                               "you specified 'never' option"))
                return None

        if overwrite in ('y', 'Y', 'all', 'ALL', 'always', 'never', 'ask'):
            if overwrite == 'always':
                msgdebug(warn=("Overwrite all existing files because "
                               "you specified the 'always' option"))
            try:
                shutil.move(os.path.join(tmpdir, track),
                            os.path.join(outputdir, track))
            # Catching too general exception Exception (FIXME)
            except Exception as err:
                return err

    return None
# ----------------------------------------------------------#


def cuefile_reading(fname, suffix):
    """
    Given a *.cue sheet file, it extracts the titles
    of the audio tracks to be split. Returns a dictionary
    with TITLE, FILE and progressive NUM keys for the
    names of the audio tracks.
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


def cuefile_check(filename: str):
    """
    Accepts an absolute or relative pathnames of a CUE file.
    Returns False if error, True otherwise.
    """
    if not os.path.isfile(filename):
        return False
    if os.path.splitext(filename)[1] not in ('.cue', '.CUE'):
        return False

    return True
# ----------------------------------------------------------#


def make_temp_dir(**kwargs):
    """
    Defines a temporary folder for working safely with files
    """
    with tempfile.TemporaryDirectory(suffix=None,
                                     prefix='pysplitcue_',
                                     dir=None) as tmpdir:

        run = run_process_splitting(kwargs['fname'],
                                    kwargs['titletracks']['FILE'],
                                    kwargs['suffix'],
                                    tmpdir
                                    )
        if run:
            msgdebug(err=f"{run}")
            sys.exit(1)

        os.chdir(tmpdir)
        runtag = run_process_tagging(kwargs['filename'], kwargs['suffix'])
        if runtag:
            msgdebug(warn=f"{runtag}")
            sys.exit(1)

        os.chdir(kwargs['dirname'])
        msbdir = make_subdir(kwargs['outputdir'])
        if msbdir is not None:
            msgdebug(err=f"{msbdir}")
            msgend(abort=True)
            sys.exit(1)

        move = move_files_on_outputdir(kwargs['outputdir'],
                                       tmpdir,
                                       kwargs['overwrite']
                                       )
        if move:
            msgdebug(err=f"{move}")
            sys.exit(1)

        msgdebug(info="Target output: ",
                 tail=f"\033[34m'{os.path.abspath(kwargs['outputdir'])}'"
                      f"\033[0m")
    msgend(done=True)
    sys.exit(0)
# ----------------------------------------------------------#


def main():
    """
    Evaluates positional arguments using the argparser module.
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
        filename = os.path.abspath(args.input_cuefile)
        dirname = os.path.dirname(filename)
        fname = os.path.basename(filename)
        there = os.path.abspath(args.outputdir)
        outputdir = there if args.outputdir != '.' else args.outputdir
        suffix = args.format_type
        overwrite = args.overwrite

        checkfile = cuefile_check(filename)
        if checkfile is False:
            msgdebug(err=f"Invalid file: '{filename}'\n"
                     f"Provide a CUE sheet file (*.cue).")
            sys.exit(1)
        else:
            os.chdir(dirname)
            titletracks = cuefile_reading(fname, suffix)

        if not titletracks:
            msgdebug(err=f"pysplitcue: error: Unable to read: '{filename}'")
            sys.exit(1)
        else:
            make_temp_dir(filename=filename,
                          dirname=dirname,
                          fname=fname,
                          outputdir=outputdir,
                          suffix=suffix,
                          overwrite=overwrite,
                          titletracks=titletracks,
                          )


if __name__ == '__main__':
    main()
