#!/usr/bin/python3

import argparse
import inspect
from typing import cast

from .utilities.ArgsNamespace import ArgsNamespace
from .utilities.CustomHelpFormatter import CustomHelpFormatter

""" 
Make sure that you have the Python KDevelop plugin installed.
"""
#Double the length for all scales we do work on to ease the indexing
ChromaticScaleSharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
#doubled sharp and flat
ChromaticScaleFlat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'G#', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'G#', 'A', 'Bb', 'B']
ChromaticScale = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
CircleoffifthsSharp = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F']
#doubled sharp and flat
CircleoffifthsFlat = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
Circleoffifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'Ab', 'Eb', 'Bb', 'F']
                              
def Majorkey(ChromaticScalein, n):
    Steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
    Nsteps = ['2', '2', '1', '2', '2', '2', '1']
    #TODO implement this in a loop
    Majorscale = [ChromaticScalein[n], ChromaticScalein[n+2], ChromaticScalein[n+4], ChromaticScalein[n+5], ChromaticScalein[n+7], ChromaticScalein[n+9], ChromaticScalein[n+11], ChromaticScalein[n+12]]
    for note in Majorscale:
        print(note+' ',end='')
def Minorkey():
    Steps = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
    Nsteps = ['2', '1', '2', '2', '1', '2', '2']
    
    
def Printtofile(key, boolean):
    
    i = 0
    while(i<len(ChromaticScale)):
        Majorkey(ChromaticScaleSharp, i)
        i += 1
        print()
    
    
def Keyparser(keyargument):
    Key = keyargument
    if len(Key) > 1:
        if Key[1] == 'b':
            for i in ChromaticScaleFlat:
                if Key == i:
                    print('The key was found in the chromatic scale! the key is: ' + Key)
                    Majorkey(Key, ChromaticScaleFlat, i)
                    #Execute logic for scales and circleoffifths
                    return True
        else:
            for i in ChromaticScaleSharp:
                if Key == i:
                    print('The key was found in the chromatic scale! the key is: ' + Key)
                    #Execute logic for scales and circleoffifths
                    return True
    if len(Key) == 1:
        for i in ChromaticScaleSharp:
            if Key == i:
                print('The key was found in the chromatic scale! the key is: ' + Key)
                #Execute logic for scales and circleoffifths
                return True
    print('Please input one of the following keys:')
    for i in ChromaticScale:
                print(i)
                return False
#The main program runs version, help, name and scales parsing
def main():
    #Start with the parser to get help arguments, version number and finally the scales argument to call the program with a key you want.
    parser = argparse.ArgumentParser(description='This project will take an input of a musical key and print the major and minor scales for it', formatter_class=CustomHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version='circleoffifths 1.0')
    parser.add_argument('-s', '--scales', help='Use this parameter to print scales from a key. usage: -s *key* will print the keys scale')
    parser.add_argument('-p', '--printtofile', action='store_true', help='Use this parameter to print all the scales from any key to a file. usage: add -p after calling -s *KEY* to print to a file')
    parser.add_argument('-a', '--all', action='store_true', help='Use this parameter to print all the scales of all the keys to a file. usage: -a')
    args: ArgsNamespace = cast(ArgsNamespace, parser.parse_args())
#Run the keyparser subprogram to check if the key is valid and execute the scale logic
#Keyparser(args.scales)
    print(args.printtofile)
    Printtofile(args.printtofile, args.printtofile)
                
        
                
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
