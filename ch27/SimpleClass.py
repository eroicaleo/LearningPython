#!/usr/bin/env python3

class rec:
    pass

rec.name = "Bob"
rec.age = 40

print(rec.name)
print(rec.age)

x = rec()
y = rec()

x.name = "Sue"
print(rec.name, x.name, y.name)

l = list(rec.__dict__.keys())
print(l)
l = list(name for name in rec.__dict__.keys() if not name.startswith('__'))
print(l)
l = list(x.__dict__.keys())
print(l)
l = list(y.__dict__.keys())
print(l)

print(x.__class__)

def uppername(obj):
    return obj.name.upper()

rec.method = uppername
l = list(name for name in rec.__dict__.keys() if not name.startswith('__'))
print(l)
print(x.method())
print(y.method())

class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        print(self.name, self.jobs)
    
Bob = Person('Bob', ['mgr', 'dev'], 40)
Bob.info()
Sue = Person('Sue', ['mgr', 'cto'])
Sue.info()
