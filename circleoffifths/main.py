#!/usr/bin/python3

import argparse
import inspect
from typing import cast

from .utilities.ArgsNamespace import ArgsNamespace
from .utilities.CustomHelpFormatter import CustomHelpFormatter

""" 
Make sure that you have the Python KDevelop plugin installed.
"""
ChromaticScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G"', 'A', 'A#', 'B']

def Majorkey():
    Steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
def Minorkey():
    Steps = ['W', 'H', 'W', 'W', 'H', 'W', 'W']

#The main program runs version, help, name and scales parsing
def main():
    parser = argparse.ArgumentParser(description='This project will take an input of a musical key and print the major and minor scales for it', formatter_class=CustomHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version='circleoffifths 1.0')
    parser.add_argument('-n', '--name', metavar='<name>', help='prints Hello There *Your name*')
    parser.add_argument('-s', '--scales', help='Use this parameter to print scales from a key. usage: -s *key* will print the keys scale')
    args: ArgsNamespace = cast(ArgsNamespace, parser.parse_args())

    for i in ChromaticScale:
        if args.scales == i:
            print('The key was found in the chromatic scale! the key is: ' + args.scales)
    
#    if args.name and args.scales:
#        print('Hello There ' + args.name + '!')
#    elif args.scales:
#        print (args.scales)
#        if args.scales == 'C':
#            print('Hello There!')
#    elif args.name:
#        print('Hello ' + args.name + '!')
#    else:
#        print('Hello World!')

# Commenting out the nonsense to work on the key scales
