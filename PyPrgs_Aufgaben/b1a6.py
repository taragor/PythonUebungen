#!/usr/bin/python3

import sys

def heron(x, e):
    a0 = ((1+x)/2)
    an = (a0 + (x/a0)/2)
    an1 = a0

    while abs(an1-an) > e:
        an1 = an
        an = ((an1 + (x/an1))/2)

    return an1

def main(args):
    if(len(args)<1):
        print("Bitte mindestens 2 argumente: x,[epsilon]")
        return
    elif(len(args)<2):
        epsilon = 10**(-6)
        x = float(args[0])
    else:
        x = float(args[0])
        epsilon = float(args[1])

    print(heron(x, epsilon))

if __name__ == '__main__':
    main(sys.argv[1:])
