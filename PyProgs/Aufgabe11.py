#!/bin/usr/python3

#12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

from functools import reduce

def main():
    array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
    #[-1, -3, -10, 2, 5, 7, 8, 9]

    result = [x for x in array_nums if x < 0] + [x for x in array_nums if x >= 0]

    result1 = list(filter(lambda x: x<0, array_nums)) + list(filter(lambda x: x>=0, array_nums))

    print(result)
    print(result1)

    pass

if __name__ == "__main__":
    main()