#!/usr/bin/env python

from linklist import *

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first, second = head, head
        while first != None:
            while first != None and first.val == second.val:
                first = first.next
            second.next = first
            second = first
        return head

sol = Solution()
l = [1, 1, 2]
l = [1]
l = [1,1,1,1,1]
l = []
l = [1,1,2,3,3]
head = linkListBuilderFromList(l)
traverse(head)
traverse(sol.deleteDuplicates(head))
