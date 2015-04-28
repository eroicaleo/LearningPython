#!/usr/bin/env python3

class FirstClass:
    def selfdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

X = FirstClass()
X.selfdata('King Authur')
X.display()

Y = FirstClass()
Y.selfdata(3.1415)
Y.display()
