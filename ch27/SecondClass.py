#!/usr/bin/env python3

import FirstClass

class SecondClass(FirstClass.FirstClass):
    def display(self):
        print('Current value = %s' % self.data)

Z = SecondClass()
Z.setdata(42)
Z.display()
