#!/bin/usr/python3

def unzip(zipped):          #zip 'transponiert' die eingegebenen Matrix; erneutes zip macht die 'transposition' rückgängig
    #liste1 = zipped[0]
    #liste2 = zipped[1]

    #print(liste1)
    #print(liste2)

    #return(list(zip(liste1, liste2)))

    return(zip(*zipped))    #zip( (1,2,3),(4,5,6) )


def add(a,b):
    print(a+b)

def main():
#    add(1,2)

#    add(*[5,6]) # == add(5,6) 

    print(unzip([(1,2,3),(4,5,6)]))
    pass

if __name__ == '__main__':
    main()