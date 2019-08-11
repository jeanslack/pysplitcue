#
# First release: 25/08/2012
# 
#########################################################
# Name: pysplitcue
# Porpose: wraps the shnsplit and cuetag commands
# Platform: Mac OsX, Gnu/Linux
# Writer: jeanslack <jeanlucperni@gmail.com>
# license: GPL3
# Rev: January 26 2015, Nov 21 2017, Nov 24 2017, Aug 8 2018
#########################################################

import sys
import os
from pysplc.str_utils import strings
from shutil import which
import argparse
import subprocess

# check to essential
if which('cuetag'):
    cuetag = which('cuetag')
elif which('cuetag.sh'):
    cuetag = which('cuetag')
else:
    sys.stderr.write("pysplitcue:ERROR: cuetag is required, "
                     "please install 'cuetools'.")
    sys.exit(1)
if not which('shntool'):
    sys.stderr.write("pysplitcue:ERROR: 'shntool' is required, "
                     "please install it.")
    sys.exit(1)
    
# add useful information strings 
cr = strings()
prg_name = cr[6]
version = cr[3]
release = cr[4]
webpage = cr[7]
blogspot = cr[8]
long_help = cr[11]
short_help = cr[12]
try_help = cr[15]

#----------------------------------------------------------#
def dependencies():
    """
    Check for dependencies
    
    """
    listing = ['flac', 'mac', 'wavpack', 'shntool', 'cuebreakpoints', 
               'cueconvert', 'cueprint']
    for required in  listing:
        #if which(required):
        if which(required, mode=os.F_OK | os.X_OK, path=None):
                
            print ("Check for: '%s' ..Ok" % required)
        else:
            print ("Check for: '%s' ..Not Installed" % required)
    
    if which('cuetag', mode=os.F_OK | os.X_OK, path=None):
        print ("Check for: 'cuetag' ..Ok")
        
    elif which('cuetag.sh', mode=os.F_OK | os.X_OK, path=None):
        print ("Check for: 'cuetag.sh' ..Ok")
    else:
        print ("Check for: 'cuetag' ..Not Installed")
            
#----------------------------------------------------------#
def run_process(in_ext, out_ext, name):
    """
    All final processes
    
    """
    in_ext = in_ext.split('.')[1]
    name = name.split('.')[0]
    split_dict = {'wav:wav':
            f'shnsplit -o wav -f {name}.cue -t "%n - %t.split" {name}.wav',
                  'wav:flac':
            f'shnsplit -o flac -f {name}.cue -t "%n - %t" {name}.wav',
                  'wav:ape':
            f'shnsplit -o ape -f {name}.cue -t "%n - %t" {name}.wav',
                  'flac:wav':
            f'shnsplit -o wav -f {name}.cue -t "%n - %t" {name}.flac',
                  'flac:flac':
            f'shnsplit -o flac -f {name}.cue -t "%n - %t" {name}.flac',
                  'flac:ape':
            f'shnsplit -o ape -f {name}.cue -t "%n - %t" {name}.flac',
                  'ape:wav':
            f'shnsplit -o wav -f {name}.cue -t "%n - %t" {name}.ape',
                  'ape:flac':
            f'shnsplit -o flac -f {name}.cue -t "%n - %t" {name}.ape',
                  'ape:ape':
            f'shnsplit -o ape -f {name}.cue -t "%n - %t.split" {name}.ape'
                 }

    tag_dict = {'wav:flac':f'{cuetag} {name}.cue *.flac', 
                'flac:flac':f'{cuetag} {name}.cue *.flac', 
                'ape:flac':f'{cuetag} {name}.cue *.flac'
                }

    if '%s:%s' %(in_ext, out_ext) in split_dict.keys():
        #print(split_dict[f'{in_ext}:{out_ext}'])#print command for debug
        try:
            command = split_dict[f'{in_ext}:{out_ext}']
            subprocess.check_call(command, shell = True)
            #makedir_move(".split.wav","Formato-wav")
            print("\033[1m...done.\033[0m")
        
        except subprocess.CalledProcessError as err:
            sys.exit("\033[31;1mProcess Error!\033[0m %s" % (err))
        
        if f'{in_ext}:{out_ext}' in tag_dict.keys():
            print("\nApply tags on audio tracks...\n")
            try:
                command = tag_dict[f'{in_ext}:{out_ext}']
                subprocess.check_call(command, shell = True)
                #makedir_move(".split.wav","Formato-wav")
                print("\033[1m...done.\033[0m")
            
            except subprocess.CalledProcessError as err:
                sys.exit("\033[31;1mProcess Error!\033[0m %s" % (err))
                
#----------------------------------------------------------#
def checker(out_ext, filename):
    """
    file check utility, evaluates if the file exists, 
    if the audio format is supported and also evaluates 
    whether the corresponding .cue file
    """
    filename = os.path.abspath(filename)
    format_list = ['.wav','.flac','.ape']
    cuelist = []
    name = os.path.basename(filename)
    in_ext = os.path.splitext(name)
    
    if os.path.isfile(filename):
        os.chdir(os.path.dirname(filename))
        for f in os.listdir():
            if os.path.splitext(f)[1] in '.cue':
                cuelist.append(f)
        
        if not in_ext[1] in format_list:
            sys.exit("pysplitcue: error: unrecognized input format '%s', "
                     "choose between  %s" % (in_ext[1],format_list))
                
        if '%s.cue' % in_ext[0] in cuelist:
            run_process(in_ext[1], out_ext, name)
        else:
            sys.exit("pysplitcue: error: No such CUE sheet file"
                     "named: '%s.cue'" % in_ext[0])
    else:
        sys.exit("pysplitcue: error: No such file: '%s'" % (filename))
        
#----------------------------------------------------------#
def main():
    """
    Parser of the users inputs (positional/optional arguments)
    """
    parser = argparse.ArgumentParser(
                description='Audio files cue splitting utility',)
    parser.add_argument(
                '-v', '--version', 
                help="show the current version and exit",
                action="store_true",
                       )
    parser.add_argument(
                '-c', '--check', 
                help="list of installed or missing dependencies",
                action="store_true",
                       )
    parser.add_argument(
                '-o',
                choices=["wav", "flac", "ape"],
                help="output audio format"
                        )
    parser.add_argument(
                '-i',
                metavar='FILE',
                #type=str, 
                help="input audio filename to splitting",
                #dest='enable_config',
                #action='store_true',
                #nargs='?',
                #default=PWD,
                #action="store_true"
                       )
    
    args = parser.parse_args()
    
    if args.check:
        dependencies()
    elif args.o:
        if not args.i:
            sys.exit('pysplitcue: error: missing option -i ..FILE')
        checker(args.o, args.i)
    elif args.version:
        print('%s - %s' % (version, release))
        return
    else:
        print("Type 'pysplitcue -h' for help.")
        
#----------------------------------------------------------#
if __name__ == "__main__":
    main()

    
