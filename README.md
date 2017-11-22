
Pysplitcue
====

## Description

A easy front-end command line interface for **Shntool** and **Cuetools**.
Small command line program for audio files cue splitting, created for amnesic 
and daytime people. Work with Wav, Flac and Ape audio formats, requires the 
presence of the '* .cue' file in the same musics tracks directory.

## License and Copyright

Copyright © 2010 - 2017 Gianluca Pernigotto   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the docs folder)

## Dependencies requires

- python >=2.6 (no python 3)
- cuebreakpoints(install cuetools)
- cueconvert  (install cuetools)
- cueprint (install cuetools)
- cuetag.sh  (install cuetools)
- shnsplit (install shntool).
- flac
- monkey's-audio (I've seen it has different names, this depends on the
                  your O.S. - try search: libmac2, mac binaries)
- wavpack

## Use

**Example:** Unzip the sources tarball of pysplitcue, open a terminal window on its path-name 
and type: `pysplitcue wav:flac '/dir/mydir/with my cue file and one track wav'`, this split 
and convert a wav audio file in a flac format. Make sure you have the *.cue* file first.

**Splitting combinations:**

for split wav to wav audio files, type option: `wav:wav` ; for split and convert wav to flac 
audio files, type option: `wav:flac` ; for split and convert ape to flac audio files, type 
option: `ape:flac` ; etc.

## Installation

pysplitcue not require installation, but if you are interested build an 
installable package, see below:

**Debian:**

Extra dependencies for build package with distutils:
`~# apt-get install python-all python-stdeb fakeroot`

Enter in unzipped sources folder and type (with not root):
`~$ python setup.py --command-packages=stdeb.command bdist_deb`

This should create a python-pysplitcue_version_all.deb in the new deb_dist directory.

see the setup.py script-file for more info on how-to build .deb package

**Slackware**

Is available a SlackBuild script to build a package *.tgz* for Slackware and Slackware based 
distributions. See here [pysplitcue.SlackBuild](https://github.com/jeanslack/slackbuilds/tree/master/pysplitcue)

Remember: first install **pysetuptools** before proceed to build Videomass, if not present.
You can search on this site: [SlackBuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

