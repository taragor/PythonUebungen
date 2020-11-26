#!/bin/usr/python3

import string
import text

def main():
    filename = "midsummernightsdream.txt"
    print(text.wc.charCount(filename))
    print(text.wc.wordCount(filename))
    print(text.wc.lineCount(filename))
    print(text.wc.wc(filename))

    text.wc.wc_show(filename, "en")

    print(text.count.count_words(filename))
    print(text.count.count_chars(filename))

    pass



if __name__ == '__main__':
    main()