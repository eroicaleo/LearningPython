#!/usr/bin/env python3

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            # print(self.stack, top)
            if isinstance(top, int):
                return True
            else:
                self.stack = self.stack[:-1] + list(top)[::-1]
        return False

nestedList = [1,[2,[3]]]
nestedList = [1,[4,[6]]]
nestedList = [[1,1],2,[1,1]]
nestedList = [[],[[]]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
