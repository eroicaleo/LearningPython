#!/usr/bin/env python3

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

X = FirstClass()
X.setdata('King Authur')
X.display()

Y = FirstClass()
Y.setdata(3.1415)
Y.display()

