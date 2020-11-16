#!/bin/usr/python3

#5. Write a Python program to filter a list of integers using Lambda. 

def main():
    integers = list(range(1,100))

    filteredList = list(filter(lambda x: x%2 == 0,integers))

    print(filteredList)

    pass

if __name__ == "__main__":
    main()