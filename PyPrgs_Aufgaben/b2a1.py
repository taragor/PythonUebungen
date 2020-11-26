#!/usr/bin/python3

import sys

def main():
    lis = list(range(0,100,1))
    print(lis[:9])
    print(lis[::10])
    print(lis[-10:])
    print(lis[len(lis)//2])
    print(lis[4:-5:3])
    print(lis[::3][4:-5])


if __name__ == "__main__":
    main()