#!/bin/usr/python3

from functools import reduce
import sys
import string

def main(args):
    args = ["abbcccaa","aaabbc","aaaabbbccdefg","aaaaaaaaaaaaaaaaaaaabb"]
    listenReduce(args)

    pass

def listenReduce(args):
    #"aabbcccaa"
    #[[a,a],[b,b],[c,c,c],[a]] //aa

    for word in args:
        liste = reduce(lambda x,y: x[:-1]+[x[-1]+[y]] if x[-1][0] == y else x+[[y]], word[1:], [[word[0]]])
        print(liste)
        ourMap = map(lambda x: x[0]+(str(len(x)) if len(x)>1 else ""),liste)
        print("".join(list(ourMap)))
        
        inEinerZeile = "".join(list(map(lambda x: x[0]+(str(len(x)) if len(x)>1 else ""),reduce(lambda x,y: x[:-1]+[x[-1]+[y]] if x[-1][0] == y else x+[[y]], word[1:], [[word[0]]]))))
        print(inEinerZeile)


def reduceLoesung(args):
    for word in args:
        kurz = reduce(lambda x,y: x+y+"1" if buchstabenAusString(x)[-1] != y else x[:-1]+str(int(x[-1])+1), word, " ")
        print(kurz)

def buchstabenAusString(x):
    bst = "".join(list(filter(lambda z: z in string.ascii_letters,x)))
    if bst == "":
        bst = " "
    return(bst)

def cLoesungSchlecht(args):
    for word in args:
        wordToDo = word[1:]
        result = ""
        searchLetter = word[0]
        i = 1
        while len(wordToDo)>0:
            if wordToDo[0]==searchLetter:
                i+=1
                wordToDo=wordToDo[1:]
            else:
                result += searchLetter 
                if i > 1:
                    result += str(i)
                i=1
                searchLetter = wordToDo[0]
                wordToDo=wordToDo[1:]
        result += searchLetter 
        if i > 1:
            result += str(i)
        i=1        
        print(result)

if __name__ == "__main__":
    main(sys.argv[1:])