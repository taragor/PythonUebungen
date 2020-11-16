#!/bin/usr/python3

#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and print the result.

import sys

def main():
    #print(list(filter((lambda x: x%2 !=0),range(1,100))))

    # add = lambda x: x+15
    # result = add(int(sys.argv[1]))

    #result = (lambda x: x+15)(int(sys.argv[1]))

    mult = lambda x,y: x*y

    print(mult(4,5))
    pass

if __name__ == "__main__":
    main()