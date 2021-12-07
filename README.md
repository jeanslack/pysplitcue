# Pysplitcue - Splitting utilities for big audio tracks supplied with CUE sheet.

Pysplitcue is a stupid wrapper for the **shntool** and **cuetools** libraries. 
It splits big audio tracks using informations contained in the associated **"CUE"** 
file. It supports Wav, Flac and Ape audio formats and auto tag. 
Requires related **'*.cue'** sheet file to read audio metadata and execute commands 
for splitting and tagging.

## Dependencies requires

- Python >=3.6
- cuetools *(includes: cuebreakpoints, cueconvert, cueprint, cuetag)*
- shntool *(includes: shnsplit)*
- flac
- mac *(monkey's-audio, name depends to your O.S., try search: libmac2, mac)*
- wavpack

## Usage

usage: `pysplitcue [-h] [-v] [-c] [-o {wav,flac,ape}] [-i FILE]`   

optional arguments:   

  `-h, --help`         show this help message and exit   
  `-v, --version`      show the current version and exit   
  `-c, --check`        list of installed or missing dependencies   
  `-o {wav,flac,ape}`  output audio format   
  `-i FILE`            input audio filename to splitting   

## Example

`pysplitcue -o flac -i file.wav`   

To split and convert wav audio format into the relative individual auto-tagged 
flac format audio tracks.

## Installation

`python3 -m pip install pysplitcue`

## License and Copyright

Copyright © 2010 - 2021 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)


