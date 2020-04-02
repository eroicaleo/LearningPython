#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

print_banner('Dog example')

class Dog:
    num_legs = 4

    def __init__(self, name):
        self.name = name

jack = Dog('Jack')
jill = Dog('Jill')
print(jack.name, jill.name)

print(f'Dog.num_legs = {Dog.num_legs}')
print(f'jack.num_legs = {jack.num_legs}')

try:
    Dog.name
except AttributeError as err:
    print(f'Got this TypeError error: {err!r}')

print_banner('Change Dog num_legs to 6')
Dog.num_legs = 6
print(f'jack.num_legs = {jack.num_legs}, jill.num_legs = {jill.num_legs}')

print_banner('Change Dog num_legs back to 4, also assign jack.num_legs to 6')
Dog.num_legs = 4
jack.num_legs = 6
print(f'Dog.num_legs = {Dog.num_legs}, jack.num_legs = {jack.num_legs}, jill.num_legs = {jill.num_legs}')
print(f'jack.num_legs = {jack.num_legs}, jack.__class__.num_legs = {jack.__class__.num_legs}')

print_banner('CountedObject')

class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

print(f'CountedObject.num_instances = {CountedObject.num_instances}')
print(f'CountedObject().num_instances = {CountedObject().num_instances}')
print(f'CountedObject().num_instances = {CountedObject().num_instances}')
print(f'CountedObject().num_instances = {CountedObject().num_instances}')
print(f'CountedObject().num_instances = {CountedObject().num_instances}')

print_banner('BuggyCountedObject')

class BuggyCountedObject:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1

print(f'BuggyCountedObject.num_instances = {BuggyCountedObject.num_instances}')
print(f'BuggyCountedObject().num_instances = {BuggyCountedObject().num_instances}')
print(f'BuggyCountedObject().num_instances = {BuggyCountedObject().num_instances}')
print(f'BuggyCountedObject().num_instances = {BuggyCountedObject().num_instances}')
print(f'BuggyCountedObject().num_instances = {BuggyCountedObject().num_instances}')
print(f'BuggyCountedObject().num_instances = {BuggyCountedObject().num_instances}')
print(f'BuggyCountedObject.num_instances = {BuggyCountedObject.num_instances}')


