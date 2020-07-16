#!/usr/bin/env python3

# 662. Maximum Width of Binary Tree
# Medium

# 1336

# 271

# Add to List

# Share
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# Note: Answer will in the range of 32-bit signed integer.

# Accepted
# 67,828
# Submissions
# 168,801

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from tree import *
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        max_width = 1
        queue = deque([(root, 1)])
        while queue:
            start, width = queue[0][1], 0
            for _ in range(len(queue)):
                node, ix = queue.popleft()
                width = ix-start+1
                if node.left:
                    queue.append((node.left, 2*ix))
                if node.right:
                    queue.append((node.right, 2*ix+1))
            print(f'width = {width}')
            max_width = max(width, max_width)
        return max_width

nodeString = '[1,3,2,5,3,null,9]'
nodeString = '[1,3,null,5,3]'
nodeString = '[1,3,2,5,null]'
nodeString = '[1,3,2,5,null,null,9,6,null,null,7]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.widthOfBinaryTree(root))
