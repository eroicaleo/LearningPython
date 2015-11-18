#!/usr/bin/env python3


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1+percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent+bonus)


if __name__ == '__main__':
    # self test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.1)
    print(sue)
    tom = Manager('Tom Jones', pay=500000)
    tom.give_raise(0.1)
    print(tom.last_name())
    print(tom)
    print('-- All Three --')
    for obj in (bob, sue, tom):
        obj.give_raise(0.1)
        print(obj)

    print(bob.__class__.__name__)
    print(list(bob.__dict__.keys()))

    for key in bob.__dict__:
        print(key, '=>', bob.__dict__[key])

    for key in bob.__dict__:
        print(key, '=>', getattr(bob, key))
