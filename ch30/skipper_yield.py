#!/usr/bin/env python

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        return
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item

alpha = 'abcde'
skipper = SkipObject(alpha)
I = iter(skipper)
print(next(I))
print(next(I))
print(next(I))

for x in skipper:
    for y in skipper:
        print(x+y, end=' ')
print()
