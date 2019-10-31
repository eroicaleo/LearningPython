#!/usr/bin/env python

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

# Error:
# foo()

foo('hello')
foo('hello', 1, 2, 3)
foo('hello', 1, 2, 3, key1='value', key2=999)

print('################################################################################')
print('## Forwarding Optional or Keyword Arguments')
print('################################################################################')

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

print(AlwaysBlueCar('green', 10000).color)

import functools

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting, name, age):
    return '{}, {}!'.format(greeting, name)

greet('Hello', 'Bob', age=50)
