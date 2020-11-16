#!/bin/usr/python3

#10. Write a Python program to create Fibonacci series upto n using Lambda. 
#0,1,1,2,3,5,8,13,21,34,55

from functools import reduce


def main():
    
    fibonacci = lambda n: reduce(lambda x, _: x+[x[-1] + x[-2]],range(n-2), [0,1])

    print(fibonacci(100))

    pass

if __name__ == "__main__":
    main()