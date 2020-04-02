#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

print_banner('MyClass example')

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())

print_banner('Call the method on the class')

print(MyClass.classmethod())
print(MyClass.staticmethod())
try:
    print(MyClass.method())
except TypeError as e:
    print(f'e = {e}')
