#!/usr/bin/env python3

from linklist import *

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import collections
        prev, stack = ListNode(0), collections.deque()
        ret, ret.next, curr, front = prev, head, head, head.next if head else None
        while curr and front:
            front = front.next
            stack.append(curr)
            stack.append(curr.next)
            curr = stack.pop()
            curr.next = stack.pop()
            curr.next.next = front
            prev.next = curr
            # traverse(curr)
            prev, curr = curr.next, front
            if front:
                front = front.next
        return ret.next

head = linkListBuilder('[1,2,3,4]')
head = linkListBuilder('[1,2,3,4,5]')
head = linkListBuilder('[1]')
head = linkListBuilder('[]')
traverse(head)
sol = Solution()
head = sol.swapPairs(head)
traverse(head)
