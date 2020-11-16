#!/bin/usr/python3

#15. Write a Python program to add two given lists using map and lambda.

def main():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6] 
    print(list(map(lambda x,y: x+y, nums1, nums2)))   

    pass

if __name__ == "__main__":
    main()