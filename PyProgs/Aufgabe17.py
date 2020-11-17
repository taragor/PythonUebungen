#!/bin/usr/python3

#17. Write a Python program 
# to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

def main():
    numbers = list(range(1,10**6))
    print(list(filter(lambda x: (x%19 == 0) or (x%13 == 0), numbers)))
    pass

if __name__ == "__main__":
    main()