#!/bin/usr/python3

from functools import reduce

def main():
    #ramanujan(5000)
    ramanujanDic(15)
    pass

def ramanujan(ubound):
    dic = {}
    for i in range(1,ubound+1):
        print(i)
        for j in range(1, i+1):
            result = i**3+j**3
            if result in dic.keys():
                dic[result] = dic[result] + (tuple(sorted((i,j))),)
            else:
                dic[result] = (tuple(sorted((i,j))),)

    for key in dic.keys():
        if len(dic[key])>1:
            print(dic[key])
            print(key)

def ramanujanDic(ubound):
    myMap = map(lambda x: (x//ubound,x%ubound,(x//ubound)**3+(x%ubound)**3), range(0,ubound**2))
    myList = [(x//ubound,x%ubound,(x//ubound)**3+(x%ubound)**3) for x in range(0, ubound**2)]
    sortedMap = sorted(myMap, key = lambda x: (x[2],min(x[0],x[1]),max(x[0],x[1])))
    reducedMap = reduce(lambda x,y: x if x[2] == y[2] and (x[1],x[0]) != (y[0],y[1]) else (x[0],x[1],-1), sortedMap)
    print(list(reducedMap)[:225])
 

if __name__ == '__main__':
    main()
