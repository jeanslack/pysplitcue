# Pysplitcue - CUE sheet splitter, based on shntool and cuetools libraries.

Pysplitcue is a stupid wrapper for the [shntool](http://freshmeat.sourceforge.net/projects/shntool) 
and [cuetools](https://github.com/svend/cuetools) libraries.
It splits big audio tracks using informations contained in the associated
**"CUE"** sheet file. It supports Wav, Flac and Ape audio formats and auto tag (only
for flac format).

## Requires

- Python >=3.6
- cuetools *(includes: cuebreakpoints, cueconvert, cueprint, cuetag)*
- shntool *(includes: shnsplit)*
- flac
- mac
- wavpack

Note for **mac** codec: monkey's-audio, name depends to your O.S., try search: libmac2, mac


## Usage
usage: `pysplitcue [-h] [--version] -i IMPUTFILE [-f {wav,flac,ape}] [-o OUTPUTDIR] [-ow {ask,never,always}] [-c]`   

```
optional arguments:
  -h, --help            show this help message and exit
  --version             Show the current version and exit
  -i IMPUTFILE, --input-cuefile IMPUTFILE
                        An absolute or relative CUE sheet file, i.e. with `.cue` extension
  -f {wav,flac,ape}, --format-type {wav,flac,ape}
                        Preferred audio format to output, default is 'flac'
  -o OUTPUTDIR, --output-dir OUTPUTDIR
                        Absolute or relative destination path for output files. If a specified 
                        destination folder does not exist, it will be created automatically. 
                        By default it is the same location as IMPUTFILE
  -ow {ask,never,always}, --overwrite {ask,never,always}
                        Overwrite files on destination if they exist, Default is `ask` before proceeding
  -c, --check-requires  List of installed or missing dependencies

```  

## Examples

`pysplitcue -i 'inputfile.cue'`   

To split and convert `wav`, `flac` or `ape` audio format into the relative individual 
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


