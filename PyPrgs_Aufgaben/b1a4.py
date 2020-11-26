#!/usr/bin/python3

def main():
    lis = [1,2]
    print(lis)
    
    lis = lis + lis
    print(lis)
    """Lis = [1, 2, 1, 2]"""

    lis = [1,2]
    lis.append(lis)
    print(lis)
    """lis = [l, 2, lis]"""

if __name__ == '__main__':
    main()