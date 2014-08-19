#!/usr/bin/env python3

def copyDict(d):
    myNewDict = dict()
    for key in d:
        myNewDict[key] = d[key]
    return myNewDict

D = {1: 'a', 2: 'b'}
myNewDict = copyDict(D)
print(D)
print(myNewDict)

myNewDict[1] = 'c'
print(D)
print(myNewDict)

D = {1: ['a', 'c'], 2: 'b'}
myNewDict = copyDict(D)
print(D)
print(myNewDict)

myNewDict[1] = ['b', 'c']
print(D)
print(myNewDict)

def addDict(d1, d2):
    myNewDict = dict()
    for key in d1:
        myNewDict[key] = d1[key]
    for key in d2:
        myNewDict[key] = d2[key]
    return myNewDict

d1 = {1: 'a'}
d2 = {2: 'b'}
myNewDict = addDict(d1, d2)
print(myNewDict)
