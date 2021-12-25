# Pysplitcue - CUE sheet splitter, based on shntool and cuetools libraries.

Pysplitcue is a stupid wrapper for the [shntool](http://freshmeat.sourceforge.net/projects/shntool) 
and [cuetools](https://github.com/svend/cuetools) libraries.
It splits big audio tracks using informations contained in the associated
**"CUE"** sheet. It supports Wav, Flac and Ape audio formats and auto tag only
for flac format. Requires related **'*.cue'** file to read audio metadata
and execute commands for splitting and tagging.

## Requires

- Python >=3.6
- cuetools *(includes: cuebreakpoints, cueconvert, cueprint, cuetag)*
- shntool *(includes: shnsplit)*
- flac
- mac *(monkey's-audio, name depends to your O.S., try search: libmac2, mac)*
- wavpack

## Usage
usage: `pysplitcue [-h] [--version] -i IMPUTFILE [-f {wav,flac,ape}] [-o OUTPUTDIR] [-ow {ask,never,always}] [-c]`   

```
optional arguments:
  -h, --help            show this help message and exit
  --version             Show the current version and exit
  -i IMPUTFILE, --input-cuefile IMPUTFILE
                        INPUTFILE must be a CUE sheet with '.cue' filename extension
  -f {wav,flac,ape}, --format-type {wav,flac,ape}
                        Preferred audio format to output, default is flac
  -o OUTPUTDIR, --output-dir OUTPUTDIR
                        Output directory, default '.'
  -ow {ask, never, always}, --overwrite {ask, never, always}
                        Overwrite files on destination if they exist, default is 'ask'
  -c, --check-requires  List of installed or missing dependencies
```  


## Example

`pysplitcue -i 'inputfile.cue'`   

To split and convert `wav` or `ape` audio format into the relative individual 
`flac` format audio tracks.   

`pysplitcue -i '/User/music/collection/inputfile.cue' -f wav -o 'my-awesome-tracklist'`   

This command splits the individual audio tracks into `wav` format 
and saves them in the 'my-awesome-tracklist' folder.   


## Installation

`python3 -m pip install pysplitcue`

## License and Copyright

Copyright © 2010 - 2021 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)


