#!/usr/bin/env python3

from tree import *
from collections import Counter

class Solution:
    def pathSum(self, root, sum):
        self.d, self.ret = {}, 0
        def dfs(root):
            if root == None:
                return Counter()
            print(f'enterting {root.val}')
            cnt = Counter({k+root.val:v for k, v in (dfs(root.left) + dfs(root.right)).items()}) + Counter({root.val: 1})
            print(f'returning {cnt}')
            self.ret += cnt[sum]
            return cnt
        dfs(root)
        return self.ret
 
root = treeBuilder('[10,5,-3,3,2,null,11,3,-2,null,1]')
traverse(root)
sum = 8
sol = Solution()
print(sol.pathSum(root, 8))
