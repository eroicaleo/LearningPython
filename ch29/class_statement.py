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


class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)

x = NextClass()
x.printer('instance call')
print(x.message)
NextClass.printer(x, 'class call')
print(x.message)


class Super:
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined!'

class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')

x = Super()
x.method()

x = Sub()
x.method()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('Starting Extender.method')
        Super.method(self)
        print('Ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for kclass in (Inheritor, Replacer, Extender):
        print('\n' + kclass.__name__ + '...')
        kclass().method()


print('\nProvider ...')
x = Provider()
x.delegate()

X = Super()
X.delegate()