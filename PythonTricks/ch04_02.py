#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

print_banner('User class without __str__ or __repr__')
my_car = Car('red', 37281)
print(my_car)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

print_banner('User class with __str__')
my_car = Car('red', 37281)
print(my_car)
print_banner('Converting to string with str() method')
print(str(my_car))
print_banner('Converting to string with \'{}\'.format method')
print('{}'.format(my_car))

print_banner('Compare between __str__ and __repr__')

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'__str__ for Car'

    def __repr__(self):
        return f'__repr__ for Car'

my_car = Car('red', 37281)
print(my_car)
print('{}'.format(my_car))
print('__repr__ will be called if you are in an interactive session')
print(str([my_car]))
print(str(my_car))
print(repr(my_car))

import datetime
today = datetime.date.today()
print(str(today))
print(repr(today))
print(type(today))

print_banner('Redefine __repr__ with don\'t repeat yourself approach')

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

my_car = Car('red', 37281)
print(my_car)
