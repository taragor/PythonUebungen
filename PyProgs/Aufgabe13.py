#!/bin/usr/python3

#13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda

def main():
    numbers = [1,2,3,4,5,6,8,10,12]
    even = len(list(filter(lambda x: x%2==0, numbers)))
    odd = len(list(filter(lambda x: x%2!=0, numbers)))

    print(even)
    print(odd)
    pass

if __name__ == "__main__":
    main()