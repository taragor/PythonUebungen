#!/bin/usr/python3

def main():
    print(list(filter(lambda y: not (y%2), map(lambda x: x**3, range(1, 11)))))
    print(map(lambda x: x**3, range(1, 11)))
    print(filter(lambda y: not (y%2), map(lambda x: x**3, range(1, 11))))
    x = 16
    print([y for y in range(2,x) if x%y == 0])

if __name__ == '__main__':
    main()