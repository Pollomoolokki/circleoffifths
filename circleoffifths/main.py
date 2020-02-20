#!/usr/bin/python3

import argparse
import inspect
from typing import cast

from .utilities.ArgsNamespace import ArgsNamespace
from .utilities.CustomHelpFormatter import CustomHelpFormatter

""" 
Make sure that you have the Python KDevelop plugin installed.
"""
ChromaticScaleSharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
ChromaticScaleFlat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'G#', 'A', 'Bb', 'B']
def Majorkey():
    Steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
    
def Minorkey():
    Steps = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
def Keyparser(keyargument):
    Key = keyargument
    if len(Key) > 1:
        if Key[1] == 'b':
            for i in ChromaticScaleFlat:
                if Key == i:
                    print('The key was found in the chromatic scale! the key is: ' + Key)
        else:
            for i in ChromaticScaleSharp:
                if Key == i:
                    print('The key was found in the chromatic scale! the key is: ' + Key)
    if len(Key) == 1:
        for i in ChromaticScaleSharp:
            if Key == i:
                print('The key was found in the chromatic scale! the key is: ' + Key)
    if len(Key) > 2:
        print('Please input a proper key. The keys are the following: ') 
        for i in ChromaticScaleFlat:
                print(i)
        for i in ChromaticScaleSharp:
                print(i)

#The main program runs version, help, name and scales parsing
def main():
    parser = argparse.ArgumentParser(description='This project will take an input of a musical key and print the major and minor scales for it', formatter_class=CustomHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version='circleoffifths 1.0')
    parser.add_argument('-n', '--name', metavar='<name>', help='prints Hello There *Your name*')
    parser.add_argument('-s', '--scales', help='Use this parameter to print scales from a key. usage: -s *key* will print the keys scale')
    args: ArgsNamespace = cast(ArgsNamespace, parser.parse_args())
    Keyparser(args.scales)
                
#    if len(args.scales) > 1:
#        if args.scales[1] == 'b':
#            for i in ChromaticScaleFlat:
#                if args.scales == i:
#                    print('The key was found in the chromatic scale! the key is: ' + args.scales)
#        else:
#            for i in ChromaticScaleSharp:
#                if args.scales == i:
#                    print('The key was found in the chromatic scale! the key is: ' + args.scales)
#    if len(args.scales) == 1:
#        for i in ChromaticScaleSharp:
#            if args.scales == i:
#                print('The key was found in the chromatic scale! the key is: ' + args.scales)
#    if len(args.scales) > 2:
#        print('Please input a proper key. The keys are the following: ') 
#        for i in ChromaticScaleFlat:
#                print(i)
#        for i in ChromaticScaleSharp:
#                print(i)
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
