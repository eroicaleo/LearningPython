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
        n1 = n2 = 0
        while l1:
            n1 = 10*n1 + l1.val
            l1 = l1.next
        while l2:
            n2 = 10*n2 + l2.val
            l2 = l2.next
        nodeList = [ListNode(int(c)) for c in str(n1+n2)] + [None]
        for i, node in enumerate(nodeList[:-1]):
            node.next = nodeList[i+1]
        return nodeList[0]

sol = Solution()
l1 = linkListBuilder('[7,2,4,3]')
l2 = linkListBuilder('[5,6,4]')
traverse(l1)
traverse(l2)
traverse(sol.addTwoNumbers(l1, l2))
