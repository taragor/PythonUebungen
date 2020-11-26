#!/usr/bin/python3

def myAppend(liste, ele):
    liste[len(liste):] += [ele]
    return liste


def main():
    print(myAppend([1,2,3], 3))

if __name__ == '__main__':
    main()