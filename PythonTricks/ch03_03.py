#!/usr/bin/env python

def null_decorator(func):
    return func

null_decorator(print)('Hello decorator!')

def greet():
    return 'Hello!'

print(null_decorator(greet)())

print('greet:', greet)
print('null_decorator(greet):', null_decorator(greet))

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet2():
    return 'Hello!'

print(greet2())
print('greet2:', greet2)
print('uppercase(greet2): ', uppercase(greet2))

print('################################################################################')
print('## Applying Multiple Decorators to a Function')
print('################################################################################')

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasize(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasize
def greet3():
    return 'Hello!'

print(greet3())

print('################################################################################')
print('## Decorating Functions That Accept Arguments')
print('################################################################################')

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

print(say('Jane', 'Hello, World!'))

print('################################################################################')
print('## How to Write “Debuggable” Decorators')
print('################################################################################')

import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a frendly greeting."""
    return 'Hello!'

print('With functools.wraps')
print('greet.__name__:', greet.__name__)
print('greet.__doc__:', greet.__doc__)

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a frendly greeting."""
    return 'Hello!'

print('Without functools.wraps')
print('greet.__name__:', greet.__name__)
print('greet.__doc__:', greet.__doc__)
