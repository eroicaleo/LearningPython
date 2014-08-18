#!/usr/bin/env python3

def keywords(good=1, bad=2, ugly=3):
    mysum = good + bad + ugly
    return mysum

print(keywords())
print(keywords(ugly=1, good=2))

def keywords2(**kargs):
    if len(kargs.keys()) == 0:
        return None
    key_list = list(kargs.keys())
    res = kargs[key_list[0]]
    for key in key_list[1:]:
        res += kargs[key]
    return res

print(keywords2(ugly=4, good=5))
print(keywords2(ugly=[1,2,3], good=[4,5]))
