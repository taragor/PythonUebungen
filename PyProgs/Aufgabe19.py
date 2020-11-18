#!/bin/usr/python3
#19. Write a Python program to find all anagrams of a string in a given list of strings using lambda

def main():
    anagrams = ["nagel", "algen", "hamster"]
    string = "gelna"

    print(list(filter(lambda x: sorted(string) == sorted(x), anagrams)))


    pass


if __name__ == "__main__":
    main()