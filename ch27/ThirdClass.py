#!/usr/bin/env python3

import SecondClass

class ThirdClass(SecondClass.SecondClass):

    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[Third class: %s]' % (self.data)

a = ThirdClass('abc')
a.display()
print(a)
