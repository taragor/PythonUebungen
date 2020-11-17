#!/bin/usr/python3

#18. Write a Python program to find palindromes in a given list of strings using Lambda.

def main():
    words = ["anna", "legovogel", "lagerregal", "palindrom", "mensch", "muegli"]
    print(list(filter(lambda x: x[::-1] == x, words)))
    pass

if __name__ == "__main__":
    # main()