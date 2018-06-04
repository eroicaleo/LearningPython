#!/usr/bin/env python

class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name
    def live(self):
        print(self.name)
    def __del__(self):
        print('Goodbye ' + self.name)

brian = Life('Brian')
brian.live()
brian = 'leretta'
