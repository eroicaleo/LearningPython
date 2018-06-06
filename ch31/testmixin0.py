#!/usr/bin/env python

from listinstance import ListInstance

class Super:
    def __init__(self):
        self.data1 = 'spam'
    def ham(self):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42
    def spam(self):
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)
