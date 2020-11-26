#!/bin/usr/python3

import sys

def main(args):
    for word in args:
        print(word + " : " + soundex(word))


def soundex(word):
    # substMatrix = LazyDict()

    # substMatrix.insert("bfpv", 1)
    # substMatrix.insert("cgjkqsxz",2)
    # substMatrix.insert("dt",3)
    # substMatrix.insert("l",4)
    # substMatrix.insert("mn",5)
    # substMatrix.insert("r",6)
    # substMatrix.insert("aeiouwyh","")

    substMatrix = {}
    substMatrix.update({x:"1" for x in "bfpv"})         
    substMatrix.update({x:"2" for x in "cgjkqsxz"})
    substMatrix.update({x:"3" for x in "dt"})
    substMatrix.update({x:"4" for x in "l"})
    substMatrix.update({x:"5" for x in "mn"})
    substMatrix.update({x:"6" for x in "r"})
    substMatrix.update({x:"" for x in "aeiouwyh"})

    lowerWord = word.lower()

    output = lowerWord[0]

    for letter in lowerWord[1:]:
        if substMatrix[letter] != output[-1]:
            output = output + substMatrix[letter]
        if(len(output)==6):
            break

    for _ in range(len(output),6):
        output = output + "0"
    return output




class LazyDict(dict):
    def insert(self, keys, value):
        for key in keys:
            self[key] = value
    # ^das + alles von dict

if __name__ == '__main__':
    main(sys.argv[1:])
