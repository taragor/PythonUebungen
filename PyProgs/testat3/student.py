#!/usr/bin/python3

from __future__ import generator_stop

def skip(lst):
    # toSkip = 0
    # i = 0
    # while True:
    #     yield lst[i%len(lst)]
    #     i+=toSkip
    #     toSkip+=1
    pass

def fill(_lst):
    if _lst==[]:
        return
    if type(_lst)==list:
        lst=(y for y in _lst)
    else:
        lst=_lst
    current = next(lst)
    yield current
    for i in lst:
        while i<current:
            current-=1
            yield current
        while i>current:
            current+=1
            yield current
