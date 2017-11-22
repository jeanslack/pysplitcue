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
  version = u'v0.6.2'
  release = u'Nov. 21 2017'
  rls_name = u"Pysplitcue"
  prg_name = u"pysplitcue"
  webpage = u"https://github.com/jeanslack/pysplitcue"
  blogspot = u"http://itamburiditux.blogspot.it/search?q=pysplitcue"
  short_decript = u'A easy front-end command line interface for **Shntool** and **Cuetools**.'
  long_desript = u"""
Small command line utility for audio files cue splitting, created for amnesic 
and daytime people. Work with Wav, Flac and Ape audio formats, requires the 
presence of the '*.cue' file in the same musics tracks directory.
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

  short_help = u"""Usage: pysplitcue [OPTION] ['PATH NAME']
Try: 'pysplitcue --help' for more information."""

  license = (u"Copyright - %s %s\n"
              "Author and Developer: %s\n"
              "Mail: %s\n\n"
              "Videomass is free software: you can redistribute\n"
              "it and/or modify it under the terms of the GNU General\n"
              "Public License as published by the Free Software\n"
              "Foundation, either version 3 of the License, or (at your\n"
              "option) any later version.\n\n"

              "Videomass is distributed in the hope that it\n"
              "will be useful, but WITHOUT ANY WARRANTY; without\n"
              "even the implied warranty of MERCHANTABILITY or\n" 
              "FITNESS FOR A PARTICULAR PURPOSE.\n" 
              "See the GNU General Public License for more details.\n\n"

              "You should have received a copy of the GNU General\n" 
              "Public License along with this program. If not, see\n" 
              "http://www.gnu.org/licenses/" %(copyright,author,
                                                author,mail))
  short_license = u"GPL3 (Gnu Public License)"
  
  return (author, mail, copyright, version, release, rls_name, prg_name, webpage, 
          blogspot, short_decript, long_desript, long_help, short_help, license,
          short_license)


