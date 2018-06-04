#!/usr/bin/env python

class PrivateExec(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExec(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Bob'

x = Test1()
# x.age = 40

y = Test2()
# y.name = 'Sue'
print(y.name)
