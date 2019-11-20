#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

print_banner('First implementation')

class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

b = Base()
try:
    b.foo()
except NotImplementedError as err:
    print(f'Got this NotImplementedError error')

c = Concrete()
print(c.foo())
try:
    c.bar()
except NotImplementedError as err:
    print(f'Got this NotImplementedError error')

print_banner('Implementation with abc module')

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

assert issubclass(Concrete, Base)

try:
    print('Instantiate b = Base()')
    b = Base()
except TypeError as err:
    print(f'Got this TypeError error: {err!r}')

try:
    print('Instantiate c = Concrete()')
    c = Concrete()
except TypeError as err:
    print(f'Got this TypeError error: {err!r}')
