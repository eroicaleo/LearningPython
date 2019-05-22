#!/usr/bin/env python3

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        from collections import deque
        stack, ret = deque(), []
        for i in nestedList:
            stack.append(i)
        while len(stack) > 0:
            i = stack.pop()
            if isinstance(i, int):
                ret.append(i)
            else:
                for j in i:
                    stack.append(j)
        self.contents = ret[::-1]
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.contents[self.index-1]
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.contents)

nestedList = [1,[2,[3]]]
nestedList = [[],[[]]]
nestedList = [[1,1],2,[1,1]]
nestedList = [1,[4,[6]]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
