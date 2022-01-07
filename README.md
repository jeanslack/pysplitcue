# Pysplitcue - CUE sheet splitter, based on shntool and cuetools libraries.

Pysplitcue is a stupid wrapper for the 
[shntool](http://freshmeat.sourceforge.net/projects/shntool) 
and [cuetools](https://github.com/svend/cuetools) libraries.
It splits big audio tracks using informations contained in the associated
**"CUE"** sheet file and can automatically handle files encoded other than 
UTF-8 and ASCII encodings without modifying the source files.    

**Note:** there are also other alternatives to pysplitcue: 
- [deflacue](https://github.com/idlesign/deflacue)
- [flacon](https://github.com/flacon/flacon)

# Features

- Supported input formats: WAV, FLAC, APE, WavPack
- Supported output formats: FLAC, APE, WAV, WavPack, OGG or MP3
- Auto-tag is supported only for FLAC, MP3, OGG formats

## Requires

- Python >=3.6
- [chardet](https://pypi.org/project/chardet/) (The Universal Character Encoding Detector)
- [shntool](http://freshmeat.sourceforge.net/projects/shntool) *(includes shnsplit)*
- [cuetools](https://github.com/svend/cuetools) *(includes cuebreakpoints, cueconvert, cueprint, cuetag)*

## Optionals
- flac 
- lame
- vorbis-tools *(includes oggenc, oggdec)*
- monkeys-audio  *(to convert APE audio format, name depends to your O.S.)*
- wavpack
 
Ubuntu users can install required and optional dependencies like this:   
`sudo apt install shntool cuetools flac lame vorbis-tools wavpack monkeys-audio`   

## Usage

#### From Command Line

```
pysplitcue -i IMPUTFILE
             [-h] 
             [--version]  
             [-f {wav, wv, flac, ape, mp3, ogg}] 
             [-o OUTPUTDIR] 
             [-ow {ask,never,always}] 
             [-c]
```

#### From Python Interpreter

```python
>>> from pysplitcue.splitcue import PySplitCue
>>> kwargs = {'filename': '/home/user/my_file.cue',
              'outputdir': '/home/user/some_other_dir',
              'suffix': 'flac',
              'overwrite': 'ask'
             }
>>> split = PySplitCue(**kwargs)
>>> split.open_cuefile()
>>> split.do_operations()
>>> split.cuefile.close()
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

Copyright © 2010 - 2022 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)


