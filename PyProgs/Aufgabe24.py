#/bin/usr/python3

#24. Write a Python program to find numbers within a given range where
#  every number is divisible by every digit it contains. 

def divisible(inchen):
    # lst = [(x,y) for x in inchen for y in [u for u in str(x) if u!='0'] if x%int(y)==0 ]
    # print(lst)

    print([x for x in inchen if all(map(lambda n: int(n) != 0 and x%int(n)==0,str(x)))])

    #1234
    #['1', '2', '3', '4']
    #[true, true, false, ....] 
def main():

    divisible(range(1,100))

    pass

if __name__ == "__main__":
    main()