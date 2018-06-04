#!/usr/bin/env python

class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

X = Empty()
print(X.age)
# print(X.name)

class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            # The following 2 works
            self.__dict__[attr] = value + 10
            # object.__setattr__(self, attr, value + 10)

            # The following 2 causes infinite loop
            # self.age = value + 10
            # setattr(self, attr, value + 10)
        else:
            raise AttributeError(attr + ' not allowed')

X = AccessControl()
X.age = 40
print(X.age)
# X.name = 'Bob'
