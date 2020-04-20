#!/usr/bin/env python3

class Node:
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.left = self.right = None

class Solution:
    def reversePairs(self, nums) -> int:
        def search(root, val):
            if not root:
                return 0
            if val < root.val:
                return root.cnt+search(root.left, val)
            elif val > root.val:
                return search(root.right, val)
            else:
                return root.cnt

        def insert(root, val):
            if not root:
                return Node(val)
            if val < root.val:
                root.left = insert(root.left, val)
            elif val > root.val:
                root.right = insert(root.right, val)
                root.cnt += 1
            else:
                root.cnt += 1
            return root

        ret, root = 0, None
        for n in nums:
            ret += search(root, 2*n+1)
            print(f'n = {n}, pairs = {search(root, 2*n+1)}')
            root = insert(root, n)
        return ret
 
sol = Solution()
nums = [1,3,2,3,1]
nums = [2,4,3,5,1]
print(sol.reversePairs(nums))
