"""
Name: str_utils
Porpose: used strings
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
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


def strings():
    """
    All general info of the pysplitcue
    """
    data = {'author': "Gianluca Pernigotto - Jeanslack",
            'mail': '<jeanlucperni@gmail.com>',
            'copyright': '© 2013-2021',
            'version': '2.0.0',
            'release': 'December 07 2021',
            'rls_name': "Pysplitcue",
            'prg_name': "pysplitcue",
            'webpage': "https://github.com/jeanslack/pysplitcue",
            'short_decript': ('Splitting utilities for big audio tracks '
                              'supplied with CUE sheet.'),
            }
    long_desript = """
Pysplitcue is a stupid wrapper for the **shntool** and **cuetools** libraries.
It splits big audio tracks using informations contained in the associated
**"CUE"** file. It supports Wav, Flac and Ape audio formats and auto tag.
Requires related **'*.cue'** sheet file to read audio metadata and execute
commands for splitting and tagging.
"""

    long_help = (f"{data['prg_name']}: {data['version']}\n"
                 f"Webpage: <{data['webpage']}>")

    short_help = "Usage: pysplitcue [OPTION] ['PATH NAME']"

    try_help = "Try: 'pysplitcue --help' for more information."

    lic = f"""
Copyright - {data['copyright']} {data['author']}
Author and Developer: {data['author']}
Mail: {data['mail']}

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License 3 as published by
the Free Software Foundation; version .

This package is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this package; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
"""

    short_license = "GPL3 (Gnu Public License)"

    return (data,
            long_desript,
            long_help,
            short_help,
            lic,
            short_license,
            try_help)
