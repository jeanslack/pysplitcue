# Pysplitcue - Splitting utilities for big audio tracks with CUE sheet.

It is a stupid wrapper interface for **Shntool** and **Cuetools** libraries.
Split big audio tracks with CUE sheet and support Wav, Flac and Ape audio 
formats and automatic tag. 
Requires a  *.cue* sheet to read audio metadata to splitting and tagging.

## Dependencies requires

- python >=3
- cuetools (includes: cuebreakpoints, cueconvert, cueprint, cuetag)
- shntool (includes: shnsplit)
- flac
- mac (monkey's-audio, name depends to your O.S., try search: libmac2, mac)
- wavpack

## Usage

usage: pysplitcue [-h] [-v] [-c] [-o {wav,flac,ape}] [-i FILE]

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show the current version and exit
  -c, --check        list of installed or missing dependencies
  -o {wav,flac,ape}  output audio format
  -i FILE            input audio filename to splitting

## Example

`pysplitcue -o flac -i file.wav`   

To splitting and conversion from wav audio format to flac audio format with
automatic tagging.

## Installation

`pip install pysplitcue`

## License and Copyright

Copyright © 2010 - 2019 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)


