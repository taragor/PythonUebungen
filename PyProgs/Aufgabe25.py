#!/bin/usr/python3

#25. Write a Python program to create the next bigger number by rearranging the digits of a given number. 

def bigger(x):
    digits = [n for n in str(x)][::-1]
    for i in range(len(digits)-1):
        if(digits[i]>digits[i+1]):
            #digits[i:i+1] = digits[i:i+1:-1]
            (digits[i], digits[i+1]) = (digits[i+1], digits[i])
            digits[0:i+1] = sorted(digits[0:i+1],reverse=True)
            break

    print(digits)       
    return(int("".join(digits[::-1])))


def main():
    print(bigger(12464321))
    pass

if __name__ == "__main__":
    main()