#!/bin/usr/python3

#20. Write a Python program to find the numbers of a given string and store them in a list, 
# display the numbers which are bigger than the length of the list in sorted form. 
# Use lambda function to solve the problem.

# Numbers in sorted form:
# 20 23 56 

def main():
    str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

    listStr = str1.split(' ')

    listNums = list(filter(lambda x: x.isdigit(), listStr))

    lenght = len(listNums)

    listEnde = list(filter(lambda x: int(x)>lenght,listNums))

    print(sorted(listEnde))

    pass

if __name__ == "__main__":
    main()