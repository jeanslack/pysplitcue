# Pysplitcue - Splitter utility for CD audio tracks.

Pysplitcue is a stupid wrapper for the **shntool** and **cuetools** libraries.
It splits big audio tracks using informations contained in the associated
**"CUE"** sheet. It supports Wav, Flac and Ape audio formats and auto tag only
for flac format. Requires related **'*.cue'** file to read audio metadata
and execute commands for splitting and tagging.

## Dependencies requires

- Python >=3.6
- cuetools *(includes: cuebreakpoints, cueconvert, cueprint, cuetag)*
- shntool *(includes: shnsplit)*
- flac
- mac *(monkey's-audio, name depends to your O.S., try search: libmac2, mac)*
- wavpack

## Usage

usage: `pysplitcue [-h] [-v] [-c] [-p {wav,flac,ape}] -i FILE.cue [-o OUTPUTDIR]`   

optional arguments:   

  `-h, --help` show this help message and exit   
  `-v, --version` Show the current version and exit   
  `-c, --check-requires` List of installed or missing dependencies   
  `-p {wav,flac,ape}, --preferred-format {wav,flac,ape}` Preferred audio format to output, default is flac   
  `-i INPUTFILE, --input-cuefile INPUTFILE` INPUTFILE must be a CUE sheet with `.cue` filename extension   
  `-o OUTPUTDIR, --output-dir OUTPUTDIR` Output directory, default '.'   


## Example

`pysplitcue -i 'FILE.cue'`   

To split and convert `wav` or `ape` audio format into the relative individual 
`flac` format audio tracks.   

`pysplitcue -i '/User/FILE.cue' -p wav -o 'my-awesome-tracklist'`   

This command splits the individual audio tracks into `wav` format 
and saves them in the 'my-awesome-tracklist' folder.   


## Installation

`python3 -m pip install pysplitcue`

## License and Copyright

Copyright © 2010 - 2021 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)


