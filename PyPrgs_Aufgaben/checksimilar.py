#!/bin/usr/python3

import sys
from soundex import soundex
import string

def main(args):
    if len(args)<1:
        print("RTFM")
        exit
    file = open(args[0],"r")
    words = file.readlines()
    
    soundexDict = {}

    for word in words:
        cleanWord = "".join([l for l in word if l in string.ascii_letters])
        
        sndX = soundex(cleanWord)
        
        soundexDict[sndX] = soundexDict.get(sndX, []) + [cleanWord]
    
    wordList = sorted(soundexDict.items(), key=lambda t: -len(t[1]))[0]

    print(wordList)

    file.close()
    pass

if __name__ == "__main__":
    main(sys.argv[1:])