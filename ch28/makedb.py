#!/usr/bin/env python3

from person import Person, Manager


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

import glob

print(glob.glob('person*'))

print(open('persondb.dir').read())
print(open('persondb.dat', 'rb').read())

db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))

bob = db['Bob Smith']
print(bob)

print(bob.last_name())

for key in db:
    print(key, '=>', db[key])

for key in sorted(db):
    print(key, '=>', db[key])

sue = db['Sue Jones']
sue.give_raise(.1)
db['Sue Jones'] = sue
db.close()

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])
db.close()
