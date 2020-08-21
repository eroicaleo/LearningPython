#!/usr/bin/env python3

from linklist import *

class Solution(object):
    def reorderList(self, head):
        if head == None:
            return
        queue = []
        while head:
            queue.append(head)
            head = head.next
        i, j = 0, len(queue)-1
        while i < j:
            queue[i].next, i = queue[j], i+1
            if i < j:
                queue[j].next, j = queue[i], j-1
        queue[j].next = None
        head = queue[0]

sol = Solution()
nodeString = '[]'
nodeString = '[1,2]'
nodeString = '[1]'
nodeString = '[1,2,3,4]'
nodeString = '[1,2,3,4,5]'
head = linkListBuilder(nodeString)
traverse(head)
sol.reorderList(head)
traverse(head)
