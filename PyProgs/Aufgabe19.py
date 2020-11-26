#!/bin/usr/python3
#19. Write a Python program to find all anagrams of a string in a given list of strings using lambda

def main():
    words = ['lager', 'egal', 'lagerr', '']
    lis = ['regal', 'egal']

    #print([list(filter(lambda x: sorted(com) == sorted(x), anagrams)) for com in string][0])

    #print([x[0] for x in filter(lambda x: x[1] == x[2],[(s1,sorted(s1),sorted(s2), s2) for s1 in words for s2 in lis]) if x[0] != x[3]])

    print([x[0] for x in filter(lambda x: x[1] == x[2],[(s1,sorted(s1),sorted(s2), s2) for s1 in words for s2 in lis]) if x[0] != x[3]])

    pass


if __name__ == "__main__":
    main()