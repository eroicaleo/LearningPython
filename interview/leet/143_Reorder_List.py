#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linklist import *

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        from collections import deque
        # put it in stack 
        if head == None or head.next == None:
            return head
        stack = deque()
        node = head
        while node:
            stack.append(node)
            node = node.next
        i, node = 0, head
        length = len(stack)
        while i < length//2:
            headNode, tailNode, node = node, stack.pop(), node.next
            headNode.next, tailNode.next = tailNode, node
            print(headNode.val)
            print(tailNode.val)
            i += 1
        if length % 2 == 1:
            tailNode, tailNode.next = tailNode.next, stack.pop()
        tailNode.next = None
        print('The final tailNode: ', tailNode.val)
        return head

sol = Solution()
nodeString = '[1,2,3,4]'
nodeString = '[1,2,3,4,5]'
nodeString = '[1,2]'
nodeString = '[1]'
nodeString = '[]'
head = linkListBuilder(nodeString)
traverse(head)
traverse(sol.reorderList(head))
