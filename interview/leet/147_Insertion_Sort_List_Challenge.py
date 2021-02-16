#!/usr/bin/env python

from linklist import *

class Solution:
    def insertionSortList(self, head):
        dumm = head
        while head:
            val, head, prev = head.val, head.next, dumm
            while val >= prev.val:
                prev = prev.next
            while prev != head:
                prev.val, prev, val = val, prev.next, prev.val
        return dumm


sol = Solution()
nodeStringList = [
        '[4,2,1,3]',
        '[-1,5,3,4,0]',
        '[3,2]',
        '[23]',
        '[]'
]
for nodeString in nodeStringList:
    head = linkListBuilder(nodeString)
    traverse(head)
    traverse(sol.insertionSortList(head))
