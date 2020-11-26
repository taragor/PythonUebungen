#!/bin/usr/python3

import string

def wc(file):
    charLen = charCount(file)
    wordLen = wordCount(file)
    lineLen = lineCount(file)
    return(charLen, wordLen, lineLen)

def wc_show(file, lang):
    lens = list(wc(file))
    langs = {"de": ["Zeichen", "Worte", "Zeilen"], "en":["Characters", "Words", "Lines"]}
    print(langs[lang][0], "\t\t", lens[0])
    print(langs[lang][1], "\t\t\t", lens[1])
    print(langs[lang][2], "\t\t\t", lens[2])

def charCount(file):
    datei = open(file, "r")

    fileLines = [line.rstrip('\n') for line in datei.readlines()]

    fullText = " ".join(fileLines)

    letters = [letter for letter in fullText if letter in string.ascii_letters]

    datei2 = open(file, "r")
    lettersFunktional = len(list(filter(lambda x: x in string.ascii_letters, " ".join(datei2.readlines()))))
    #print("LetterFunktional", lettersFunktional)

    datei.close()
    datei2.close()
    return(lettersFunktional)

def wordCount(file):
    datei = open(file, "r")

    words = " ".join(datei.readlines()).split(" ")

    datei.close()

    return(len(words))

def lineCount(file):
    datei = open(file, "r")
    length = len(datei.readlines())
    datei.close()
    return(length)