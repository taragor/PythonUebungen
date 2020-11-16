#!/bin/usr/python3

#6. Write a Python program to square and cube every number in a given list of integers using Lambda.

def main():
    numbers = list(range(1,100))

    squaredCubed = list(map(lambda x: (x, x**2, x**3),numbers))

    print(squaredCubed)

    pass

if __name__ == "__main__":
    main()