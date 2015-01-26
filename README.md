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
- Open a terminal window in unziped folder and type:

		pysplitcue wav:flac '/dir/mydir/with my cue file and one track wav'

this split and convert a wav audio file in a flac format.

Splitting combinations:

.wav to .wav

		wav:wav

.wav to .ape  

		flac:wav

.flac to .flac

		flac:ape

.ape to .wav

		ape:flac

.ape to .ape

		ape:ape

etc.

Installation
-------

pysplitcue not require installation, but if you are interested build an 
installable package, see below:

* DEBIAN:

Extra dependencies for build package with distutils:

		apt-get install python-all python-stdeb fakeroot

(see the setup.py script-file for more info on how-to build .deb package)

* SLACKWARE:

First require pysetuptools at: [slackbuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

Is available a SlackBuild script to build package .tgz or .gz for Slackware distribution that you can see at:

[my slackbuild repository](https://github.com/jeanslack/My-Repo-Slackware/tree/master/slackware/multimedia/pysplitcue)

If you want download entire content directory quickly, open a terminal window in a your path and type:

		svn checkout https://github.com/jeanslack/My-Repo-Slackware/trunk/slackware/multimedia/pysplitcue

Then download the Videomass tarball source code at:

[https://github.com/jeanslack/pysplitcue/releases](https://github.com/jeanslack/pysplitcue/releases)

..and place it into slackbuild folder.

For instructions on how to use the SlackBuilds, see:

[http://slackbuilds.org/howto/](http://slackbuilds.org/howto/)

[http://www.slackwiki.com/SlackBuild_Scripts](http://www.slackwiki.com/SlackBuild_Scripts)

[http://www.slacky.eu/slacky/Slackware_%26_SlackBuild](http://www.slacky.eu/slacky/Slackware_%26_SlackBuild)

Remember: first install pysetuptools

--------------------------------------------------------------------------------
The installation includes a man page
