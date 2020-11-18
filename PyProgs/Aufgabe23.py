#!/bin/usr/python3

#23. Write a Python program to calculate the sum of the positive and 
# negative numbers of a given list of numbers using lambda function.

def main():
    nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]

    sumPos = sum(filter(lambda x: x>0, nums))
    sumNeg = sum(filter(lambda x: x<0, nums))

    print(sumPos)
    print(sumNeg)

    pass

if __name__ == "__main__":
    main()