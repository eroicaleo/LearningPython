#!/usr/bin/env python3

X = 99

def selector():
    import __main__
    print(__main__.X)
    X = 88
    print(X)

selector()
