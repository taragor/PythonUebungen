#!/bin/usr/python3

import string

def count_words(fileName):
    file = open(fileName, "r")
    listAlleBuchstabenmitLeerzeichen = list(filter(lambda x: x in string.ascii_letters + " ", " ".join(file.readlines())))
    wortListe = "".join(listAlleBuchstabenmitLeerzeichen).split(" ")
    #{"wort1": 4, "wort2", 5}
    dic={}
    for word in wortListe:
        dic[word] = dic.get(word,0)+1

    file.close()
    return(dic)

def count_chars(fileName):
    file = open(fileName, "r")
    listAlleBuchstabenmitLeerzeichen = list(filter(lambda x: x in string.ascii_letters, " ".join(file.readlines())))
    file.close()
    dic={}
    for letter in listAlleBuchstabenmitLeerzeichen:
        dic[letter] = dic.get(letter,0)+1
    return(dic)