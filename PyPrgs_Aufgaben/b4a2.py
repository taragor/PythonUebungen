#!/bin/usr/python3

def main():
    ramanujan(5000)
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

    

if __name__ == '__main__':
    main()