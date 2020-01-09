#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

print_banner('Plain tuple')

tuple = ('hello', object(), 42)
print(tuple)
print(tuple[2])
try:
    tuple[2] = 23
except TypeError as err:
    print(f'Got this TypeError error: {err!r}')

print_banner('namedtuple')

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
print(Car)

Car = namedtuple('Car', [
    'color',
    'mileage',
])

print(Car)

my_car = Car('red', 3812.4)
print(my_car)
print(my_car.color)
print(my_car.mileage)

print(f'Access trough index: {my_car[0]}, {my_car[1]}')
print(f'String representation: {my_car}')
print('tuple unpacking:', *my_car)

print_banner('Immutable')

try:
    print('Set the color of my_car to blue')
    my_car.color = 'blue'
except AttributeError as err:
    print(f'Got this error: {err!r}')

print_banner('Add method to namedtuple')

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 1234)
print(c)
print(f'Calling method hexcolor {c.hexcolor()}')

print_banner('Add fields')
print(Car._fields)

ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
print(ElectricCar)
ev = ElectricCar('red', 1234, 45)
print(ev)

print_banner('Built-in helper functions')

print(f'_asdict: {my_car._asdict()}')
print(f'_replace: {my_car._replace(color="blue")}')
print(f'_make: {my_car._make(["yellow", 9999])}')
quit()

