#!/usr/bin/env python

def yell(text):
    return text.upper() + '!'

print(yell('hello'))

# Functions are objects

bark = yell
print(bark('woof'))

del yell
print(bark('hey'))
# error
# print(yell('hello'))
print(bark.__name__)
print(bark.__qualname__)

funcs = [bark, str.lower, str.capitalize]
print(funcs)
for f in funcs:
    print(f, f('hey there'))
print(funcs[0]('hey yo'))

def greet(func):
    greeting = func('Hi, I am a python programmer')
    print(greeting)

greet(bark)

def whisper(text):
    return text.lower() + '...'

greet(whisper)

print(list(map(bark, ['hello', 'hey', 'hi'])))

def speak(text):
    def whisper(text):
        return text.lower() + '...'
    return whisper(text)

print(speak('Hello, World'))

def get_speak_func(volumn):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volumn > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func(0.8))
print(get_speak_func(0.3))
print(get_speak_func(0.8)('Hello'))
print(get_speak_func(0.3)('Hello'))

def get_speak_func(text, volumn):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volumn > 0.5:
        return yell
    else:
        return whisper

def make_adder(n):
    def adder(x):
        return x+n
    return adder

plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4))
print('If bark is callable?', callable(bark))
print('If plus_3 is callable?', callable(plus_3))
print('If \'hello\' is callable?', callable('hello'))
