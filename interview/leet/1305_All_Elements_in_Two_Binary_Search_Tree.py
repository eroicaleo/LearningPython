#!/usr/bin/env python3

from tree import *

class Solution:
    def getAllElements(self, root1, root2):
        def sortBst(node):
            ret, stack = [], []
            while node or stack:
                while node:
                    node, stack = node.left, stack+[node]
                node = stack.pop()
                ret, node = ret+[node.val], node.right
            return ret
        list1, list2 = sortBst(root1), sortBst(root2)
        l1, l2 = len(list1), len(list2)
        i1 = i2 = 0
        ret = []
        while i1 < l1 or i2 < l2:
            if i1 == len(list1):
                i2, ret = i2+1, ret+[list2[i2]]
            elif i2 == len(list2):
                i1, ret = i1+1, ret+[list1[i1]]
            elif list2[i2] < list1[i1]:
                i2, ret = i2+1, ret+[list2[i2]]
            else:
                i1, ret = i1+1, ret+[list1[i1]]
        return ret

    # votrubac's solution
    def getAllElements_2(self, root1, root2):
        def pushLeft(stack, node):
            while node:
                stack.append(node)
                node = node.left
        stack1, stack2 = [], []
        pushLeft(stack1, root1)
        pushLeft(stack2, root2)
        ret = []
        while stack1 or stack2:
            if len(stack2) == 0:
                s = stack1
            elif len(stack1) == 0:
                s = stack2
            elif stack2[-1].val < stack1[-1].val:
                s = stack2
            else:
                s = stack1
            n = s.pop()
            ret.append(n.val)
            pushLeft(s, n.right)
        return ret

sol = Solution()
root1 = treeBuilder('[2,1,4]')
root2 = treeBuilder('[1,0,3]')
traverse(root1)
traverse(root2)
print(sol.getAllElements_2(root1, root2))
