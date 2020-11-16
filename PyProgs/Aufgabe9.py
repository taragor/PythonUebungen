#!/bin/usr/python3

#9. Write a Python program to check whether a given string is number or not using Lambda.

def main():

    isNumber = lambda x: x in '0123456789'

    print(isNumber('1'))
    print(isNumber('a'))

    pass


if __name__ == "__main__":
    main()