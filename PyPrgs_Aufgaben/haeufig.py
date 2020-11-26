#!/bin/usr/python3

import text

def main():
    fileName = "./midsummernightsdream.txt"
    wordDic = text.count.count_words(fileName)
    charDic = text.count.count_chars(fileName)

    print(top25(wordDic))
    print(top25(charDic))
    pass

def top25(dic):
    tup = list(dic.items())
    sortedTup = sorted(tup, key=lambda x: x[1], reverse = True)
    return(sortedTup[:25])

if __name__ == '__main__':
    main()