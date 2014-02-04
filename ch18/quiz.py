#!/usr/local/bin/python3.3

def func(a, b=4, c=5):
    print(a, b, c)

func(1, 2)

def func(a, b, c=5):
    print(a, b, c)

func(1, c=3, b=2)

def func(a, *pargs):
    print(a, pargs)

func(1, 2, 3)

def func(a, **kargs):
    print(a, kargs)

func(a=1, c=3, b=2)

def func(a)
