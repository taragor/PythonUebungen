#!/usr/bin/python3
import sys

def calc(v1, op, v2):
    if(op == "+"):
        return(float(v1) + float(v2))
    elif(op == "-"):
        return(float(v1) - float(v2))
    elif(op == "*"):
        return(float(v1) * float(v2))
    elif(op == "/"):
        return(float(v1) / float(v2))
    else:
        print("Bitte rechenzeichen eingeben")
        exit

def main(args):
    if(len(args) == 3):
        print(calc(args[0], args[1], args[2]))
    else:
        print("Bitte genau 3 Argumente eingeben")
    


if __name__ == "__main__":
    main(sys.argv[1:])