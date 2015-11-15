#!/usr/bin/env python3


class rec:
    pass

rec.name = 'Bob'
rec.age = 40

print(rec.name)

x = rec()
y = rec()

print(x.name, y.name)

x.name = 'Sue'

print(x.name, y.name, rec.name)

print(list(rec.__dict__.keys()))
l = [name for name in rec.__dict__ if not name.startswith('__')]
print(l)
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))

print(x.name, x.__dict__['name'])
print(x.age)

# KeyError: 'age'
# print(x.__dict__['age'])

print(x.__class__)
print(rec.__bases__)


def uppername(obj):
    return obj.name.upper()

print(uppername(x))

rec.method = uppername
print(x.method())
print(y.method())
print(rec.method(x))


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return self.name, self.jobs

rec1 = Person('Bob', ['dev', 'mgr'], 40)
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs)
print(rec2.info())
