#!/usr/bin/env python

from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class Htmlize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('trispam.txt', 'r'), sys.stdout)
    obj.process()

    prog = Uppercase(open('trispam.txt', 'r'), open('trispamup.txt', 'w'))
    prog.process()

    Uppercase(open('trispam.txt', 'r'), Htmlize()).process()
