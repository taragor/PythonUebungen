#!/bin/usr/pyhton3

#Using list comprehension, construct a list from the squares of each element in the list.

def main():
    lst1=[2, 4, 6, 8, 10, 12, 14]

    #Type your answer here.

    lst2=[x**2 for x in lst1]


    print(lst2)
    pass

if __name__ == "__main__":
    main()