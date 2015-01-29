================================================================================ 
A cue splitter audio files
================================================================================ 

Small and useful command line program for cue splitting audio files 
when ripped on one track (with cue-file) to preserve fidelity to
Original CompactDisk.
This work with Wav, Flac and Ape audio formats and if need its enable 
to decode / encode audio-tracks.
Requires the presence of the * .cue file in the same directory music track

--------------------------------------------------------------------------------

Copyright © 2010 - 2015 Gianluca Pernigotto 
 
  Author and Developer: Gianluca Pernigotto 
  Mail: <jeanlucperni@gmail.com>
  License: GPL3 (see LICENSE file in the docs folder)

--------------------------------------------------------------------------------

Dependencies requires:

	python >=2.6 (no python 3)
	
Dependencies recommended:

	flac
	cuetools
	shntool
	mac or monkeys-audio
	wavpack
	
Use
-------

- Unzip the sources tarball of pysplitcue
- Open a terminal window in unzipped folder and type:

		pysplitcue wav:flac '/dir/mydir/with my cue file and one track wav'

this split and convert a wav audio file in a flac format.


Splitting combinations:

.wav to .wav

		wav:wav

.wav to .ape  

		wav:ape

.flac to .flac

		flac:flac

.ape to .flac

		ape:flac

.ape to .ape

		ape:ape

etc.

Installation
-------

pysplitcue not require installation, but if you are interested build an 
installable package, see below:


--------------------------------------------------------------------------------

DEBIAN:

--------------------------------------------------------------------------------

Extra dependencies for build package with distutils:

		# apt-get install python-all python-stdeb fakeroot

Enter in unzipped sources folder and type (with not root):

		python setup.py --command-packages=stdeb.command bdist_deb

This should create a python-pysplitcue_version_all.deb in the new deb_dist directory.

see the setup.py script-file for more info on how-to build .deb package

--------------------------------------------------------------------------------

SLACKWARE:

--------------------------------------------------------------------------------

Require pysetuptools at: [slackbuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

Then download the SlackBuild: [My-Repo-Slackware](https://github.com/jeanslack/My-Repo-Slackware/tree/master/slackware/multimedia/pysplitcue)


--------------------------------------------------------------------------------
The installations includes a man page
--------------------------------------------------------------------------------

