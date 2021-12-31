# Pysplitcue - CUE sheet splitter, based on shntool and cuetools libraries.

Pysplitcue is a stupid wrapper for the 
[shntool](http://freshmeat.sourceforge.net/projects/shntool) 
and [cuetools](https://github.com/svend/cuetools) libraries.
It splits big audio tracks using informations contained in the associated
**"CUE"** sheet file.   

# Features

- Supported input formats: WAV, FLAC, APE, WavPack
- Supported output formats: FLAC, WAV, WavPack, OGG or MP3
- Auto-tag is supported only for FLAC, MP3 and OGG formats

## Requires

- Python >=3.6
- cuetools *(includes cuebreakpoints, cueconvert, cueprint, cuetag)*
- shntool *(includes shnsplit)*
- flac
- lame
- vorbis-tools *(include oggenc, oggdec)*
- mac  *(monkey's-audio, name depends to your O.S.)*
- wavpack

**Note:** If you are satisfied with only getting files in `flac` format, there is 
a better alternative to pysplitcue: [deflacue](https://github.com/idlesign/deflacue). 
Also, if you prefer to use a GUI instead of the command line, check out 
[flacon](https://github.com/flacon/flacon) as well.


## Usage
usage: `pysplitcue [-h] [--version] -i IMPUTFILE [-f {wav, wv, flac, ape, mp3, ogg}] [-o OUTPUTDIR] [-ow {ask,never,always}] [-c]`   

```
optional arguments:
  -h, --help            show this help message and exit
  --version             Show the current version and exit
  -i IMPUTFILE, --input-cuefile IMPUTFILE
                        An absolute or relative CUE sheet file, i.e. with `.cue` extension
  -f {wav, wv, flac, ape, mp3, ogg}, --format-type {wav, wv, flac, ape, mp3, ogg}
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

To split and convert several audio formats into the relative individual 
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


