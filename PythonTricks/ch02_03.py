#!/usr/bin/env python

import time
from contextlib import contextmanager

class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

@contextmanager
def program_timer():
    try:
        start_time = time.time()
        yield
    finally:
        stop_time = time.time()
        print('I am in decorator: %.4f seconds passed' % (stop_time - start_time))

with program_timer():
    j = 0
    for i in range(1000000):
        j += 1

class Indenter:
    def __init__(self):
        self.indent_level = -4
    def __enter__(self):
        self.indent_level += 4
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_level -= 4
    def print(self, msg):
        print(self.indent_level*' '+msg)

class ProgramTimer:
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = time.time()
        print('%.4f seconds passed' % (self.stop_time - self.start_time))

with ProgramTimer():
    j = 0
    for i in range(1000000):
        j += 1

with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello!')
        with indent:
            indent.print('bonjour')
    indent.print('hey')

with ManagedFile('hello.txt') as f:
    f.write('hello world!')
    f.write('bye!')

with managed_file('hello2.txt') as f:
    f.write('hello world 2!\n')
    f.write('bye!\n')


