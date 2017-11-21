#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#
#
#########################################################
# Name: str_utils
# Porpose: used string
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2017 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
#########################################################


def strings():

  prg_name = "Pysplitcue"
  version = "Version 0.6, released 25/08/2012)"
  webpage = "https://github.com/jeanslack/pysplitcue"
  blogspot = "http://itamburiditux.blogspot.it/search?q=pysplitcue"
  short_decript = 'A easy command line interface for shntool.'
  long_desript = """
Small and useful command line program for audio files cue splitting, 
created for amnesic and daytime people.
Work with Wav, Flac and Ape audio formats, requires the presence of 
the '* .cue' file in the same musics tracks directory.
"""

  long_help = """%s: %s
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
    pysplitcue ape:wav '/path name/My directory/'""" % (prg_name, version,
                                                        webpage,blogspot)

  short_help = """Usage: pysplitcue [OPTION] ['PATH NAME']
Try: 'pysplitcue --help' for more information."""
  
  return (prg_name, version, webpage, blogspot, long_help, short_help)
