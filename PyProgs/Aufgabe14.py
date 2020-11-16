#!/bin/usr/python3

#14. Write a Python program to find the values of length six in a given list using Lambda.

def main():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    result = filter(lambda x: len(x)==6,weekdays)

    print(list(result))

    pass


if __name__ == "__main__":
    main()