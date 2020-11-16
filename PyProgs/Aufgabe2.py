#!/bin/usr/python3

#2. Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.

def funcGenerator(unknown):
    return(lambda x: x*unknown)

def main():
    

    print((funcGenerator(7))(3))
    pass

if __name__ == "__main__":
    main()