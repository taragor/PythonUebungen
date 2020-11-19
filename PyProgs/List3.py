#!/bin/usr/pyhton3

#Use list comprehension to construct a new list but add 6 to each item.

def main():
    #Type your answer here.

    lst1=[44,54,64,74,104]

    lst2=[x+6 for x in lst1]


    print(lst2)
    pass

if __name__ == "__main__":
    main()