#!/bin/usr/python3

import sys
from soundex import soundex
import string

def main(args):
    if len(args)<2:
        print("RTFM")
        exit
    file = open(args[1],"r")
    words = file.readlines()
    for word in words:
        cleanWord = ""
        for letter in word:
            if letter in list(string.ascii_letters):
                cleanWord = cleanWord + letter

        if soundex(args[0]) == soundex(cleanWord):
            print(cleanWord)
    

    file.close()
    pass

if __name__ == "__main__":
    main(sys.argv[1:3])