#!/usr/bin/env python

from tree import *
import linklist

class Solution:
    def buildTree(self, head): 
        if head == None:
            return
        r_tail, root, l_tail = head, head, None
        while r_tail.next != None: 
            if r_tail.next != None:
                r_tail = r_tail.next
            if r_tail.next != None:
                r_tail = r_tail.next
                l_tail = root
                root = root.next
        l_head = head if l_tail else None
        if l_tail:
            l_tail.next = None
        r_head = root.next
        root.next = None

        root_node = TreeNode(root.val)
        root_node.left, root_node.right = self.buildTree(l_head), self.buildTree(r_head)

        print('root, r_head, l_head:')
        linklist.traverse(root)
        linklist.traverse(r_head)
        linklist.traverse(l_head)

        return root_node

sol = Solution()

l = []
l = [-10]
l = [-10,-3]
l = [-10,-3,0]
l = [-10,-3,0,5]
l = [-10,-3,0,5,9]
head = linklist.linkListBuilderFromList(l)
linklist.traverse(head)
traverse(sol.buildTree(head))
