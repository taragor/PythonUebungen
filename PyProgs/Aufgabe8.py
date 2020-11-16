#!/bin/usr/python

#8. Write a Python program to extract year, month, date and time using Lambda.

import datetime

def main():
    myBirthdate = datetime.date(1998, 8, 14)

    myBirthdayParty = datetime.datetime(2021,8,14,15,30,00)

    getDate = lambda x: x.year
    # getMonth = 
    # getYear = 
    # getTime = 

    print(getDate(myBirthdate))

    pass


if __name__ == "__main__":
    main()