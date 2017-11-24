#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#
#
#########################################################
# Name: str_utils
# Porpose: used string
# Writer: jeanslack <jeanlucperni@gmail.com>
# license: GPL3
#########################################################


def strings():
  """
  All general info of the pysplitcue
  """
  author = u"Gianluca Pernigotto - Jeanslack"
  mail = u'<jeanlucperni@gmail.com>'
  copyright = u'© 2013-2017'
  version = u'v0.6.3'
  release = u'Nov. 24 2017'
  rls_name = u"Pysplitcue"
  prg_name = u"pysplitcue"
  webpage = u"https://github.com/jeanslack/pysplitcue"
  blogspot = u"http://itamburiditux.blogspot.it/search?q=pysplitcue"
  short_decript = u'A stupid wrapper interface for **Shntool** and **Cuetools** libraries.'
  long_desript = u"""
Audio files cue splitting utilities, created for amnesic and daytime 
people. Work with Wav, Flac and Ape audio formats, requires the presence 
of the cue sheet metadata ( *.cue* filename extension) in the same musics 
tracks directory.
"""

  long_help = u"""%s: %s
Webpage: <%s>
Blogspot: <%s>

Usage: pysplitcue  [OPTION] [PATH-NAME]

  *  The argument OPTION is mandatory

    wav:wav        Spitting from .wav to .wav
    wav:flac       Spitting and conversion from .wav to .flac
    wav:ape        Spitting and conversion from .wav to .ape

    flac:wav       Spitting and conversion from .flac to .wav
    flac:flac      Splitting from flac to flac
    flac:ape       Spitting and conversion from .flac to .ape

    ape:wav        Spitting and conversion from .ape to .wav
    ape:flac       Spitting and conversion from .ape to .flac
    ape:ape        Splitting from ape to ape

  *   The argument PATH-NAME is not mandatory
    
    The splitting cue process start if there are audio and cue files
    in the current directory

OTHER OPTIONS:  
    -h, --help            Print this help and exit
    -v, --version         Print the program version and date

EXAMPLES:
    pysplitcue flac:wav
    pysplitcue wav:flac /path/name/
    pysplitcue ape:wav '/path name/My directory/'
    """ % (prg_name, version, webpage, blogspot)

  short_help = u"Usage: pysplitcue [OPTION] ['PATH NAME']"
  
  try_help = u"Try: 'pysplitcue --help' for more information."

  license = u"""
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

  short_license = u"GPL3 (Gnu Public License)"
  
  return (author, mail, copyright, version, release, rls_name, prg_name, webpage, 
          blogspot, short_decript, long_desript, long_help, short_help, license,
          short_license, try_help)


