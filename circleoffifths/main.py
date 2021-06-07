#!/usr/bin/python3

import argparse
import inspect
from typing import cast

from .utilities.ArgsNamespace import ArgsNamespace
from .utilities.CustomHelpFormatter import CustomHelpFormatter

""" 
Make sure that you have the Python KDevelop plugin installed.
"""
#Testing commit on windows
#Double the length for all scales we do work on to ease the indexing
#Originally I wanted to search for the key and reconstruct the list so it starts from the given key. It was not a success, however I found doubling the length of the scales to be an effective way to circumvent this problem.
ChromaticScaleSharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
#doubled sharp and flat
ChromaticScaleFlat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
#This is only used for printing help if a wrong key is given and checking the length of the scale
ChromaticScale = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
CircleoffifthsSharp = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F']
#doubled sharp and flat
CircleoffifthsFlat = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
Circleoffifthsmajor = ['C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb', 'C#/Db', 'Ab', 'Eb', 'Bb', 'F']
Circleoffifthsmajorsharp = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'Ab', 'Eb', 'Bb', 'F']
Circleoffifthsmajorflat = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']
#Lets make a list for major and minor circleoffifths. index is so that every n for major is it's relative minor in Circleoffifthsminor
Circleoffifthsminor = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'Eb/D#', 'Bb', 'F', 'C', 'G', 'D']
Circleoffifthsminorsharp = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'Bb', 'F', 'C', 'G', 'D']
Circleoffifthsminorflat = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'Eb', 'Bb', 'F', 'C', 'G', 'D']

def circleoffifths(ChromaticScalein, n):
    Sharps = [6]
    Flats = [6]
    
    
def Majorkey(ChromaticScalein, n):
    Steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
    Nsteps = [2, 2, 1, 2, 2, 2, 1]
    #TODO implement this in a loop or with Nsteps
    #Sidenote: It makes awfully stupid code to use Nsteps. For example last index would be ChromaticScalein[n+[Nsteps[0]+Nsteps[1]+Nsteps[2]+...] etc. Dunno if Nsteps[0+7] is doable
    #After some research - it is possible to call sum(0:len(Nsteps)) so the code would be something like: x=0 for i in Majorscale | i = ChromaticScalein[n+sum(Nsteps(0:x))] | x += 1
    Majorscale = [ChromaticScalein[n], ChromaticScalein[n+2], ChromaticScalein[n+4], ChromaticScalein[n+5], ChromaticScalein[n+7], ChromaticScalein[n+9], ChromaticScalein[n+11], ChromaticScalein[n+12]]
    print('Major scale notes:')
    for note in Majorscale:
        print(note+' ',end='')
    print()

def Minorkey(ChromaticScalein, n):
    Steps = ['W', 'H', 'W', 'W', 'H', 'W', 'W']
    Nsteps = [2, 1, 2, 2, 1, 2, 2]
    Minorscale = [ChromaticScalein[n], ChromaticScalein[n+2], ChromaticScalein[n+3], ChromaticScalein[n+5], ChromaticScalein[n+7], ChromaticScalein[n+8], ChromaticScalein[n+10], ChromaticScalein[n+12]]
    print('Minor scale notes:')
    for note in Minorscale:
        print(note+' ',end='')
    print()

def Printtofile(key, boolean):
#WORK IN PROGRESS
#Next up is printing to file
#TODO Print to a file. Either every key scale with -p or one scale with -p *KEY*
    i = 0
    while(i<len(ChromaticScale)):
        Majorkey(ChromaticScaleSharp, i)
        i += 1
        print()
    i = 0
    while(i<len(ChromaticScale)):
        Minorkey(ChromaticScaleSharp, i)
        i += 1
        print()
    
def Keyparser(keyargument):
#TODO Print the relative minor key scale and print out the major scale keys (1,2,3,4,5,6,7) 1,3,5 being major, 2,4,6 minor and 7 diminished/7th using circleoffifths
    Key = keyargument
    #x is used for ChromaticScale index. y is for Circleoffifthsmajor index and z for Circleoffifthsminor index
    #k is used for checking the relative minor key
    x = 0
    y = 0
    z = 0
    k = ''
    if len(Key) > 1:
        if Key[1] == 'b':
            for i in ChromaticScaleFlat:
                if Key == i:
                    x = ChromaticScaleFlat.index(i)
                    print('The key was found in the chromatic scale! the key is: ' + Key)
                    #Print the scale for majorkey. We know it's flat because of earlier if statement
                    Majorkey(ChromaticScaleFlat, x)
                    #Check where the key is on circleoffifths
                    z = Circleoffifthsminorflat.index(i)
                    #Use Sharps
                    if z <=6:
                        Minorkey(ChromaticScaleSharp, x)
                    #Use Flats
                    if z > 6:
                        Minorkey(ChromaticScaleFlat, x)
                    #Print the relative minor key
                    y = Circleoffifthsmajorflat.index(i)
                    k = Circleoffifthsminorflat[y]
                    print('The relative minor key is :', k)
                    return True
        else:
            print('Please input one of the following keys:')
            for i in ChromaticScale:
                print(i, end=' ')
            print()
            return False
        if Key[1] == '#':
            for i in ChromaticScaleSharp:
                if Key == i:
                    x = ChromaticScaleSharp.index(i)
                    print('The key was found in the chromatic scale! the key is: ' + Key)
                    Majorkey(ChromaticScaleSharp, x)
                    z = Circleoffifthsminorsharp.index(i)
                    if z <=6:
                        Minorkey(ChromaticScaleSharp, x)
                    if z > 6:
                        Minorkey(ChromaticScaleFlat, x)
                    y = Circleoffifthsmajorsharp.index(i)
                    k = Circleoffifthsminorsharp[y]
                    print('The relative minor key is :', k)
                    #Execute logic for scales and circleoffifths
                    return True
        else:
            print('Please input one of the following keys:')
            for i in ChromaticScale:
                print(i, end=' ')
            print()
            return False
    if len(Key) == 1:
        for i in Circleoffifthsmajor:
            if Key == i:
                print('The key was found in the chromatic scale! the key is: ' + Key)
                y = Circleoffifthsmajor.index(i)
                z = Circleoffifthsminor.index(i)
                #Check the position for Key.
                if y <= 6:
                    x = ChromaticScaleSharp.index(i)
                    Majorkey(ChromaticScaleSharp, x)
                    k = Circleoffifthsminorsharp[y]
                if z <= 6:
                    x = ChromaticScaleSharp.index(i)
                    Minorkey(ChromaticScaleSharp, x)
                if y > 6:
                    x = ChromaticScaleFlat.index(i)
                    Majorkey(ChromaticScaleFlat, x)
                    k = Circleoffifthsminorflat[y]
                if z > 6:
                    x = ChromaticScaleFlat.index(i)
                    Minorkey(ChromaticScaleFlat, x)
                #Execute logic for scales and circleoffifths
                print('The relative minor key is :', k)
                #Think about circleoffifths
                return True
    else:
        print('Please input one of the following keys:')
        for i in ChromaticScale:
            print(i, end=' ')
        print()
        return False
    
#The main program runs version, help, name and scales parsing. It also runs the subprograms to print or save scales from given key.
def main():
    #Start with the parser to get help arguments, version number and finally the scales argument to call the program with a key you want.
    parser = argparse.ArgumentParser(description='This project will take an input of a musical key and print the major and minor scales for it', formatter_class=CustomHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version='circleoffifths 1.0')
    parser.add_argument('-s', '--scales', help='Use this parameter to print scales from a key. usage: -s *key* will print the keys scale')
    parser.add_argument('-p', '--printtofile', action='store_true', help='Use this parameter to print all the scales from any key to a file. usage: add -p after calling -s *KEY* to print to a file')
    parser.add_argument('-a', '--all', action='store_true', help='Use this parameter to print all the scales of all the keys to a file. usage: -a')
    args: ArgsNamespace = cast(ArgsNamespace, parser.parse_args())
#TODO Think about the logic for calling -p and -s
#TODO Possible solution - print all to file  once? Make a new circleoffifths.py and import logic...?
#Run the keyparser subprogram to check if the key is valid and execute the scale logic printing major and minor scales from given key
    Keyparser(args.scales)
#Run the printtofile subprogram to print major and minor scales from all keys

    #Printtofile(args.printtofile, args.printtofile)
                
        
                
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
