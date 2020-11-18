#!/bin/usr/python3

#22. Write a Python program that sums the length of the names of a given list of names 
# after removing the names that starts with an lowercase letter. Use lambda function.

from functools import reduce

def main():
    sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

    upperNames = filter(lambda y: y[0].isupper(), sample_names)



    print(reduce(lambda x,y: x+len(y),upperNames, 0))
    pass

if __name__ == "__main__":
    main()