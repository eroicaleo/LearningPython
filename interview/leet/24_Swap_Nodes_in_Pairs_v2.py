#!/usr/bin/env python3

from linklist import *

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next

head = linkListBuilder('[1,2,3,4,5]')
head = linkListBuilder('[1,2,3,4]')
head = linkListBuilder('[1]')
head = linkListBuilder('[]')
traverse(head)
sol = Solution()
head = sol.swapPairs(head)
traverse(head)
