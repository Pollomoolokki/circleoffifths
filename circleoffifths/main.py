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
ChromaticScale = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
CircleoffifthsSharp = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F']
CircleoffifthsFlat = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
Circleoffifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'Ab', 'Eb', 'Bb', 'F']
def Majorkey(Keyin, ChromaticScalein, n = int()):
    Steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
    Nsteps = ['2', '2', '1', '2', '2', '2', '1']
    Linkerlist = [0 for z in range(12)]
    Newscale = [0 for y in range(8)]
#First rearrange the scale to make sure no out of bounds things happen
    
    
    x = 0
    k = 0
    while(n<len(ChromaticScalein)):
        Linkerlist[k] = ChromaticScalein[n]
        x = k
        k += 1
        n += 1
    while(x<(len(ChromaticScalein) - n)):
        u = x - n
        Linkerlist[x] = ChromaticScalein.index[u]
        x += 1
    for i in Linkerlist:
        print(i)
def Minorkey():
    Steps = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
    Nsteps = ['2', '1', '2', '2', '1', '2', '2']
    
    
def Printtofile(key, boolean):
    
    i = 0
    while(i<len(ChromaticScaleSharp)):
        Majorkey(ChromaticScaleSharp[i], ChromaticScaleSharp, i)
        i += 1
    
    
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
    parser.add_argument('-p', '--printtofile', action='store_true', help='Use this parameter to print all the scales from any key to a file or terminal. usage: -p for terminal, -p true for a file')
    args: ArgsNamespace = cast(ArgsNamespace, parser.parse_args())
#Run the keyparser subprogram to check if the key is valid and execute the scale logic
#   Keyparser(args.scales)
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
