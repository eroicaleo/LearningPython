#!/usr/bin/env python

from tree import *

# From the discussion forum, another solution is to use pre-order and reverse
# the output

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, leftStack, rightStack, node = [], [], [], root
        while (node != None) or len(leftStack) > 0:
            while node != None:
                leftStack.append(node)
                print('I am inserting %d into leftStack: %s' % (node.val, [n.val for n in leftStack]))
                node = node.left
            node = leftStack[-1]
            if len(rightStack) == 0 or rightStack[-1] != node:
                rightStack.append(node)
                print('I am inserting %d into rightStack: %s' % (node.val, [n.val for n in rightStack]))
                node = node.right
            elif rightStack[-1] == node:
                leftStack.pop(-1)
                rightStack.pop(-1)
                print('I am popping %d from leftStack: %s' % (node.val, [n.val for n in leftStack]))
                print('I am popping %d from rightStack: %s' % (node.val, [n.val for n in rightStack]))
                ret.append(node.val)
                node = None
        return ret

nodeString = '[1,null,2,3]'
nodeString = '[]'
nodeString = '[1,4,2,3]'
sol = Solution()
root = treeBuilder(nodeString)
traverse(root)
print(sol.postorderTraversal(root))
