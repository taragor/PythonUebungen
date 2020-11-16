#!/bin/usr/python3

#3. Write a Python program to sort a list of tuples using Lambda.



def main():
    subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

    gibDasHintereAus = lambda x: x[1]

    #gibDasHintereAus = lambda x: -x[1]

    #sortedMarks = sorted(subject_marks, key= gibDasHintereAus)[::-1]

    sortedMarks = sorted(subject_marks,key= gibDasHintereAus, reverse=True)

    print(sortedMarks)
    pass

if __name__ == "__main__":
    main()