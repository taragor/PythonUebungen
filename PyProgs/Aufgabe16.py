#!/bin/usr/python3
#16. Write a Python program to find the second lowest grade of any student(s) 
# from the given names and grades of each student using lists and lambda. 
# Input number of students, names and grades of each student

# Input number of students:  5
# Name:  S ROY
# Grade:  1
# Name:  B BOSE
# Grade:  3
# Name:  N KAR
# Grade:  2
# Name:  C DUTTA
# Grade:  1
# Name:  G GHOSH
# Grade:  1

# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]

# Second lowest grade:  2.0

# Names:
# N KAR

def main():
    i = int(input("Anzahl = "))
    
    listeName = []

    for _ in range(i):
        listeName.append((input("Name = "),int(input("Note = "))))

    print(sorted(listeName, key=lambda x: x[1])[-2])

    pass

if __name__ == "__main__":
    main()