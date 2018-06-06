#!/usr/bin/env python

class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                self.__class__.__name__,
                id(self),
                self.__attrnames()
                )


if __name__ == '__main__':
    class C(ListInstance): pass
    x = C()
    x.a, x.b, x.c = 1, 2, 3
    print(x)
