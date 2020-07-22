#!/usr/bin/env python3

from linklist import *

class Solution:
    def removeElements(self, head, val):
        if head == None:
            return head
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head

nodeString = '[1,2,6,3,4,5,6]'
nodeString = '[6]'
nodeString = '[]'
head = linkListBuilder(nodeString)
val = 6
traverse(head)
sol = Solution()
traverse(sol.removeElements(head, 6))
