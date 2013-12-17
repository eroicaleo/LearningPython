#!/usr/local/bin/python3.3

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['mgr', 'dev'], age=40)
print(rec)

import json

print(json.dumps(rec))

S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)
print(rec == O)

json.dump(rec, fp=open('testjason.txt', 'w'), indent=4)
print(open('testjason.txt', 'r').read())
P = json.load(open('testjason.txt', 'r'))
print(P)
