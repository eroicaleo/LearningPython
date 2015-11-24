#!/usr/bin/env python3


class SharedData:
    spam = 42

x = SharedData()
y = SharedData()

print(x.spam, y.spam)

SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)

x.spam = 88
print(x.spam, y.spam, SharedData.spam)


class MixedNames:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)

x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()
