#!/bin/usr/pyhton3

import sys

def main(args):
    args = ["ein", "Text", "wird", "ein", "Beispiel", "das", "danach", "weggeworfen", "wird"]
    dochNichtWieC(args)
    
    pass

def dochNichtWieC(args):
    dic = {}
    for arg in args:
        dic[arg] = dic.get(arg,0) + 1 
    unsereListe = list(sorted(dic.items(), key=lambda x: (-x[1],x[0])))
    for tup in unsereListe:
        if tup[1] >= unsereListe[0][1]:
            print(tup[1], ": ", tup[0])

if __name__ == "__main__":
    main(sys.argv)