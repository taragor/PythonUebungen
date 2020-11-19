#!/bin/usr/pyhton3

#Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.

def main():
    rng = range(1200,2001,130)
    lst = [x for x in rng]
    print(lst)
    pass

if __name__ == "__main__":
    main()