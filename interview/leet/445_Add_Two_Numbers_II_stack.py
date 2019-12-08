#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linklist import *

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        import collections
        stack1, stack2 = collections.deque(), collections.deque()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        add1, head = 0, None
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            summmation = (val1+val2+add1)
            node = ListNode(summmation%10)
            add1 = summmation//10
            head, node.next = node, head
        if add1:
            node = ListNode(add1)
            head, node.next = node, head
        return head

sol = Solution()
l1 = linkListBuilder('[7,2,4,3]')
l2 = linkListBuilder('[5,6,4]')
l1 = linkListBuilder('[1]')
l2 = linkListBuilder('[9,9]')
traverse(l1)
traverse(l2)
traverse(sol.addTwoNumbers(l1, l2))
