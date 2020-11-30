#!/bin/usr/python3

def main():
    lstComp()
    print(list(filter(lambda y: not (y%2), map(lambda x: x**3, range(1, 11)))))
    print(map(lambda x: x**3, range(1, 11)))
    print(filter(lambda y: not (y%2), map(lambda x: x**3, range(1, 11))))
    x = 123
    print(list(filter(lambda y: x%y==0, range(2,x))))
    print(list(filter(lambda x: len(list(filter(lambda y: x%y==0, range(2,x))))==0, range(10000,10101))))
    

def lstComp():
    print([x**3 for x in range(1,11) if x**3%2==0])
    x = 123
    print([y for y in range(2,x) if x%y == 0])
    print([x for x in range(10000,10100) if len([y for y in range(2,x) if x%y == 0]) == 0])


if __name__ == '__main__':
    main()