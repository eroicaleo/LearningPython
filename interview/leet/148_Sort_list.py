#!/usr/bin/env python3

from linklist import *

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        l1, l2 = self.splitList(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        traverse(l1)
        traverse(l2)
        l = self.mergeList(l1,l2)
        traverse(l)
        return l

    def splitList(self, head):
        l1 = l2 = head
        while l2.next and l2.next.next:
            l1, l2 = l1.next, l2.next.next
        l1.next, l2 = None, l1.next
        return (head, l2)

    def mergeList(self, l1, l2):
        curr = head = ListNode(0)
        while l1 or l2:
            if not l1:
                head.next, l2 = l2, l2.next
            elif not l2:
                head.next, l1 = l1, l1.next
            elif l2.val < l1.val:
                head.next, l2 = l2, l2.next
            else:
                head.next, l1 = l1, l1.next
            head = head.next
        return curr.next

sol = Solution()
head = linkListBuilder('[4,2,3,1,5,6]')
head = linkListBuilder('[4,2]')
head = linkListBuilder('[4,2,3]')
head = linkListBuilder('[4,2,3,1]')
head = linkListBuilder('[]')
head = linkListBuilder('[1,3,5,2,4,6]')
head = linkListBuilder('[4,2,3,1,5]')
head = linkListBuilder('[4,2,3,1,5,6,7,8]')
head = linkListBuilder('[4]')
# traverse(head)
sol.sortList(head)
