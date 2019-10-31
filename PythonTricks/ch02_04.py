#!/usr/bin/env python

# from my_module import *
import my_module

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

class Test2:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23

t = Test()
print(t.foo)
print(t._bar)

t2 = Test2()
print(dir(t2))

# print(external_func())
# print(_internal_func())

print(my_module.external_func())
print(my_module._internal_func())

def make_object(name, class_):
    pass

class ExtendedClass(Test2):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

t2 = ExtendedClass()
print(t2.foo)
print(t2._bar)
print(dir(t2))
# Give error
# print(t2.__baz)
print(t2._ExtendedClass__baz)
print(t2._Test2__baz)

class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

print(ManglingTest().get_mangled())

class MangledMethod:
    def __method(self):
        return 42
    def call_it(self):
        return self.__method()

print(MangledMethod().call_it())
print(dir(ManglingTest()))
print(dir(MangledMethod))

_MangledGlobal__mangled = 23

class MangledGlobal:
    def test(self):
        return __mangled

print("MangledGlobal:", MangledGlobal().test())

class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

print("PrefixPostfixTest:", PrefixPostfixTest().__bam__)

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print('car color:', color)
print('car mileage:', mileage)

20+3
list()
print(_)
