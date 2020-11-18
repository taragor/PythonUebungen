#!/bin/usr/python3

#21. Write a Python program that multiply each number of given list with a given number using lambda function. 
# Print the result.

def main():
    numbers = [21, 12, 17, 8, 4, 31, 5]

    y = 4

    print(list(map(lambda x: x * y, numbers)))

    pass

if __name__ == "__main__":
    main()