#!/bin/usr/pyhton3

# Given dictionary is consisted of vehicles and their weights in kilograms. 
# Contruct a list of the names of vehicles with weight below 5000 kilograms. 
# In the same list comprehension make the key names all upper case.



def main():
    dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

    #Type your answer here.

    lst2 = [x for x in dict]

    print(lst2)

    lst=[x.upper() for x in dict.keys() if dict[x]<5000]

    print(lst)
    pass

if __name__ == "__main__":
    main()