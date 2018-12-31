#!/usr/bin/env python

from linklist import *

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        curr = head
        for i in range(n):
            curr = curr.next
        prev = curr
        curr = head
        if prev == None:
            return curr.next
        while prev.next != None:
            prev = prev.next
            curr = curr.next
        curr.next = curr.next.next
        return head

sol = Solution()
nodeStringList = [
        '[1,2,3,4,5]',
        '[1,2]'
]
for nodeString in nodeStringList:
    head = linkListBuilder(nodeString)
    traverse(head)
    traverse(sol.removeNthFromEnd(head, 2))
