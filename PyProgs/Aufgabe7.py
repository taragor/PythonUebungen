#!/bin/usr/python3
    
#7. Write a Python program to find if a given string starts with a given character using Lambda. 

def startsWithGenerator(n):
    return lambda x: x[0] == n

def main():

    startsWithS = startsWithGenerator('m')

    print(startsWithS("sophia"))
    print(startsWithS("max"))

    pass 

if __name__ == "__main__":
    main()