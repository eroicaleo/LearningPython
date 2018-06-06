#!/usr/bin/env python

def factory(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job = None):
        self.name = name
        self.job = job

object1 = factory(Spam)
object2 = factory(Person, 'Arthur', 'King')
object3 = factory(Person, name='Brian')

object1.doit(99)
print(object2.name, object2.job)
print(object3.name, object3.job)
