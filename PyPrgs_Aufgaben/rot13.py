#!/usr/bin/python3

import string
import sys

def lowerRot13():
    letters = list(string.ascii_lowercase)
    dic = {}
    for i in range(0, len(letters)):
        dic[letters[i]] = letters[(i+13)%len(letters)]
    return dic

def upperRot13():
    letters = list(string.ascii_uppercase)
    dic = {}
    for i in range(0, len(letters)):
        dic[letters[i]] = letters[(i+13)%len(letters)]  #1:a 
    return dic

def rot13(text):
    lowerSubst = lowerRot13()
    upperSubst = upperRot13()

    subst = {**lowerSubst, **upperSubst}

    outputText = ""

    for letter in text:
        if letter in subst.keys():
            outputText = outputText + subst[letter]
        else:
            outputText = outputText + letter
    return outputText


def main(arg):
    print(rot13(arg[0]))

if __name__ == '__main__':
    main(sys.argv[1:])