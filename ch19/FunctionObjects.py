#!/usr/local/bin/python3.3

def echo(message):
    print(message)
    return

echo('Direct Call')
x = echo
x('Indirect Call')

def indirect(func, arg):
    func(arg)

indirect(echo, "Argument Call")

schedule = [(echo, 'Spam'), (echo, 'Ham')]

for (func, arg) in schedule:
    func(arg)

def make(label):
    def echo(message):
        print(label + ': ' + message)
    return echo

F = make('Spam')
F('Eggs')
F('Ham')

def func(a):
    b = 'spam'
    return b * a
print(func(8))
print(dir(func))
func.handles = 'Bottom-Press'
func.count = 0
print(dir(func))

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a+b+c

print(func.__annotations__)
