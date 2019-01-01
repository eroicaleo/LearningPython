#!/usr/bin/env python

from linklist import *

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        newHead, head = head, head.next
        newHead.next = None
        while head != None:
            curr, head = head, head.next
            curr.next = None
            next = newHead
            while (next.val < curr.val) and (next.next != None):
                next = next.next
            if next.val >= curr.val:
                next.val, curr.val = curr.val, next.val
                next.next, curr.next = curr, next.next
            elif next.next == None:
                next.next = curr
        return newHead

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
