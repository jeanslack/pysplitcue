"""
Name: str_utils
Porpose: used string
Writer: jeanslack <jeanlucperni@gmail.com>
license: GPL3
"""


def strings():
  """
  All general info of the pysplitcue
  """
  author = "Gianluca Pernigotto - Jeanslack"
  mail = '<jeanlucperni@gmail.com>'
  copyright = '© 2013-2019'
  version = '1.0.1'
  release = 'December 06 2021'
  rls_name = "Pysplitcue"
  prg_name = "pysplitcue"
  webpage = "https://github.com/jeanslack/pysplitcue"
  blogspot = "http://itamburiditux.blogspot.it/search?q=pysplitcue"
  short_decript = 'A stupid wrapper interface for **Shntool** and **Cuetools** libraries.'
  long_desript = """
Splitting utilities for big audio tracks with CUE sheet.
It support Wav, Flac and Ape audio formats and automatic tag.
Requires a  *.cue* sheet to read audio metadata to splitting and tagging.
"""

  long_help = """%s: %s
Webpage: <%s>
Blogspot: <%s>
    """ % (prg_name, version, webpage, blogspot)

  short_help = "Usage: pysplitcue [OPTION] ['PATH NAME']"

  try_help = "Try: 'pysplitcue --help' for more information."

  license = """
Copyright - %s %s
Author and Developer: %s
Mail: %s

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
""" % (copyright, author, author, mail)

  short_license = "GPL3 (Gnu Public License)"

  return (author, mail, copyright, version, release, rls_name, prg_name, webpage,
          blogspot, short_decript, long_desript, long_help, short_help, license,
          short_license, try_help)
