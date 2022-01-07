"""
First release: 25/08/2012

Name: splitcue.py
Porpose: wraps the shnsplit and cuetag commands
Platform: MacOs, Gnu/Linux, FreeBSD
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
Rev: January 06 2022
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
import shutil
import subprocess
import tempfile
import chardet
from pysplitcue.str_utils import msgdebug, msgend
from pysplitcue.exceptions import InvalidFile, ParserError, TempProcessError


class PySplitCue():
    """
    This class implements an interface to securely wrap shnsplit
    and cuetag tools: Since neither shnsplit nor cuetag correctly
    support reading CUE sheet files with encodings other than
    ASCII/UTF-8, the PySplitCue class allows you to get around this
    problem by working in a temporary context without modifying the
    source files.

    Other useful functions of the PySplitCue class can
    be configured: you can choose between 6 audio output formats;
    you can set an output folder; you can control overwriting of
    files. For more details see the doc string of the constructor
    of this class.

    Usage:
            >>> from pysplitcue.splitcue import PySplitCue
            >>> kwargs = {'filename': '/home/user/my_file.cue',
                          'outputdir': '/home/user/some_other_dir',
                          'suffix': 'flac',
                          'overwrite': 'ask'
                          }
            >>> split = PySplitCue(**kwargs)
            >>> split.open_cuefile()
            >>> split.do_operations()
            >>> split.cuefile.close()
    """
    def __init__(self,
                 filename=str(''),
                 outputdir=str('.'),
                 suffix=str('flac'),
                 overwrite=str('ask')
                 ):
        """
            'filename': absolute or relative CUE sheet file
            'outputdir': absolute or relative pathname to output files
            'suffix': output format, one of "wav", "wv", "flac",
                      "ape", "mp3", "ogg"
            'overwrite': controls for overwriting files,
                         one of "ask", "never", "always"
                         Also see `move_files_on_outputdir`
                         method.
        """
        self.kwargs = {'filename': os.path.abspath(filename)}
        self.kwargs['dirname'] = os.path.dirname(self.kwargs['filename'])
        if outputdir == '.':
            self.kwargs['outputdir'] = self.kwargs['dirname']
        else:
            self.kwargs['outputdir'] = os.path.abspath(outputdir)
        self.kwargs['suffix'] = suffix
        self.kwargs['overwrite'] = overwrite
        self.cuefile = None

        filesuffix = os.path.splitext(self.kwargs['filename'])[1]
        isfile = os.path.isfile(self.kwargs['filename'])

        if not isfile or filesuffix not in ('.cue', '.CUE'):
            raise InvalidFile(f"Invalid CUE sheet file: "
                              f"'{self.kwargs['filename']}'")

        os.chdir(self.kwargs['dirname'])

        with open(self.kwargs['filename'], 'rb') as file:
            self.bdata = file.read()
            self.encoding = chardet.detect(self.bdata)
    # ----------------------------------------------------------#

    def move_files_on_outputdir(self):
        """
        All files are processed in a /temp folder. After the split
        operation is complete, all tracks are moved from /temp folder
        to output folder. Here evaluates what to do if files already
        exists on output folder.
        This method is called by `do_operations` method. Do not call
        this method directly.
        Raises:
            TempProcessError
        Returns:
            None otherwise.

        """
        outputdir = self.kwargs['outputdir']
        overwrite = self.kwargs['overwrite']

        for track in os.listdir(self.kwargs['tempdir']):
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
                    shutil.move(os.path.join(self.kwargs['tempdir'], track),
                                os.path.join(outputdir, track))
                # Catching too general exception Exception (FIXME)
                except Exception as error:
                    raise TempProcessError(error) from error

        return None
    # ----------------------------------------------------------#

    def run_process_tagging(self):
        """
        Run `cuetag` command.
        This method is called by `do_operations` method.
        Do not call this method directly.
        Raises:
            TempProcessError
        Returns:
            None otherwise.
        """
        if shutil.which('cuetag'):
            cuetag = shutil.which('cuetag')
        elif shutil.which('cuetag.sh'):
            cuetag = shutil.which('cuetag.sh')
        else:
            raise TempProcessError("'cuetag' is required, please "
                                   "install 'cuetools'.")

        if self.kwargs['suffix'] in ('flac', 'mp3', 'ogg'):
            msgdebug(info="Apply tags on audio tracks...")
            cmd_tag = (f'{cuetag} "{self.kwargs["cuefile"]}" '
                       f'*.{self.kwargs["suffix"]}'
                       )
            try:
                subprocess.run(cmd_tag, check=True, shell=True)

            except subprocess.CalledProcessError as error:
                raise TempProcessError(error) from error

            else:
                msgdebug(info="...done tagging")
        else:
            msgdebug(warn=(f"Unsupported file format "
                           f"'{self.kwargs['suffix']}' for tagging  ..skip"))
    # ----------------------------------------------------------#

    def run_process_splitting(self):
        """
        Run `shnsplit` command which is an alias to `shntool split`:
        -f file Specifies a file from which to read split point data.
        -d dir Specify output directory
        -o str Specify  output file format extension, encoder and
        arguments surrounded by quotes. If arguments are given,
        then one of them must contain "%f"
        -t fmt Name output files in user‐specified format based on CUE
        sheet fields:
                            %p Performer
                            %a Album
                            %n Track number
                            %t Track title

        This method is called by `do_operations` method. Do not call
        this method directly.
        Raises:
            TempProcessError
        Returns:
            None otherwise.
        """
        if not shutil.which('shntool'):
            #return "'shntool' is required, please install it."
            raise TempProcessError("'shntool' is required, please install it.")

        name = os.path.splitext(self.kwargs['titles']['FILE'])[0]
        inext = os.path.splitext(self.kwargs['titles']['FILE'])[1]

        mode = {'flac': 'flac flac -V --best -o %f -',
                'wav': 'wav',
                'mp3': 'cust ext=mp3 lame --quiet - -o %f -',
                'ogg': 'cust ext=ogg oggenc -b 192 -o %f -',
                'ape': 'ape',
                'wv': 'wv',
                }
        cmd_split = (f'shnsplit -f "{self.kwargs["cuefile"]}" -o '
                     f'"{mode[self.kwargs["suffix"]]}" -t "%n - %t" '
                     f'-d "{self.kwargs["tempdir"]}" "{name}{inext}"'
                     )

        msgdebug(info="splitting audio tracks...")
        try:
            subprocess.run(cmd_split, check=True, shell=True)

        except subprocess.CalledProcessError as error:
            #return error
            raise TempProcessError(error) from error

        else:
            msgdebug(info="...done splitting")
    # ----------------------------------------------------------#

    def do_operations(self):
        """
        Defines a temporary folder for working safely with files.
        This method calls following methods of this class:
            - self.run_process_splitting()
            - self.run_process_tagging()
            - self.move_files_on_outputdir
        """
        with tempfile.TemporaryDirectory(suffix=None,
                                         prefix='pysplitcue_',
                                         dir=None) as tmpdir:
            self.kwargs['tempdir'] = tmpdir
            self.run_process_splitting()
            os.chdir(tmpdir)
            self.run_process_tagging()
            os.chdir(self.kwargs['dirname'])
            try:
                os.makedirs(self.kwargs['outputdir'],
                            mode=0o777, exist_ok=True)
            except Exception as error:
                # Catching too general exception Exception (FIXME)
                raise TempProcessError(error) from error

            self.move_files_on_outputdir()
            msgdebug(info="Target output: ",
                     tail=(f"\033[34m"
                           f"'{os.path.abspath(self.kwargs['outputdir'])}'"
                           f"\033[0m"))
        msgend(done=True)
# ----------------------------------------------------------#

    def cuefile_parser(self, cuelines):
        """
        Given a cuelines list, it extracts the titles
        of the audio tracks to be split.

        Args:
            cuelines: A list containing the text lines of the
                      cuefile previously encoded with utf-8 .
        Returns:
            A dictionary with FILE and TRACK keys, where FILE is the
            name of audio file associated with cue sheet file, and
            TRACK is a progressive digit of any audio track.
            A empty dictionary otherwise.

        Raises:
            ParserError: if found invalid data
        """
        num = 'TITLE'
        titletracks = {}

        for line in cuelines:
            if 'FILE' in line:
                titletracks['FILE'] = line.split('"')[1]

            if 'TRACK' in line:
                num = line.strip().split()[1]

            if '    TITLE' in line:
                title = line.split('"')[1]
                titletracks[num] = (f"{num} - {title}.{self.kwargs['suffix']}")

        if not titletracks or not titletracks.get('FILE'):
            raise ParserError(f'Invalid data found: {titletracks}')

        return titletracks
    # ----------------------------------------------------------#

    def open_cuefile(self):
        """
        Defines a temporary UTF-8 encoded CUE sheet file,
        which is used for splitting and tagging operations .
        """
        self.cuefile = tempfile.NamedTemporaryFile(suffix='.cue',
                                                   mode='w+',
                                                   encoding='utf-8'
                                                   )
        self.cuefile.write(self.bdata.decode(self.encoding['encoding']))
        self.cuefile.seek(0)
        self.kwargs['cuefile'] = self.cuefile.name
        self.kwargs['titles'] = self.cuefile_parser(self.cuefile.readlines())
