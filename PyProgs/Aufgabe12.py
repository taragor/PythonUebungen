#!/bin/usr/python3

#1. Write a Python program to find intersection of two given arrays using Lambda.

def main():
    array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
    array_nums2 = [1, 2, 4, 8, 9]
    result = filter(lambda x: x in array_nums1, array_nums2)

    print(list(result))
    pass

if __name__ == "__main__":
    main()