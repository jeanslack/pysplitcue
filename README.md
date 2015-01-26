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

Splitting combinations from:

	.wav to .wav
	.wav to .flac
	.wav to .ape  
	.flac to .wav
	.flac to .flac
	.flac to .ape
	.ape to .wav
	.ape to .flac
	.ape to .ape
	
--------------------------------------------------------------------------------

Dependencies requires:

	python >=2.6 (no python 3)
	
Dependencies recommended:

	flac
	cuetools
	shntool
	mac or monkeys-audio
	wavpack
	
--------------------------------------------------------------------------------

pysplitcue is not require installation, but if you are interested build an 
installable package, see below:

Extra dependencies for build package with distutils:

	DEBIAN:
			apt-get install python-all python-stdeb fakeroot
			
			(see the setup.py script-file for more info on 
			how-to build .deb package)
			
	SLACKWARE:
				pysetuptools
				(http://slackbuilds.org/repository/14.1/python/pysetuptools/)
				
				Is available a SlackBuild script to build package .tgz or .gz 
				for Slackware distribution that you can download at:
				https://github.com/jeanslack/My-Repo-Slackware/tree/master/slackware/multimedia/pysplitcue
				
				If you want download entire content directory quickly, open a terminal
				window in a your path and type:
				svn checkout https://github.com/jeanslack/My-Repo-Slackware/trunk/
				slackware/multimedia/pysplitcue
				
				Then download the Videomass tarball source code at:
				http://jeanslack.github.io/Videomass/downloads.html
				..and place it into slackbuild folder.
				
				For instructions on how to use the SlackBuilds, see:
				http://slackbuilds.org/howto/
				http://www.slackwiki.com/SlackBuild_Scripts
				http://www.slacky.eu/slacky/Slackware_%26_SlackBuild
				
				Remember: first install setuptools
--------------------------------------------------------------------------------
The installation includes a man page
--------------------------------------------------------------------------------
