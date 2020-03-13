#!/usr/bin/env python3

class Solution:
    def permutation(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        ret = []
        for i in set(nums):
            ix = nums.index(i)
            ret += [[i] + m for m in self.permutation(nums[:ix]+nums[ix+1:])]
        return ret

    def permutation_stefan(self, nums):
        """
        This is non-recursive bottom up approach
        The commented part is the regular for-loop
        The real code is the
        """
        perms = [[]]
        # for n in nums:
        #     print(f'n = {n}')
        #     new_perms = []
        #     for p in perms:
        #         print(f'p = {p}, (p+[n]).index(n) = {(p+[n]).index(n)}')
        #         for i in range((p+[n]).index(n)+1):
        #             tmp = p[:i] + [n] + p[i:]
        #             print(f'tmp = {tmp}')
        #             new_perms.append(tmp)
        #     perms = new_perms
        #     print(f'perms = {perms}')
        for n in nums:
            perms = [p[:i]+[n]+p[i:] for p in perms for i in range((p+[n]).index(n)+1)]
        return perms

    def permutation_stefan(self, nums):
        from functools import reduce
        return reduce(lambda perms, n: [p[:i]+[n]+p[i:] for p in perms for i in range((p+[n]).index(n)+1)], nums, [[]])

sol = Solution()
l = [1]
l = [1,1,2]
l = []
l = [1,2,3]

print(([]+[0]).index(0))
print(sol.permutation(l))
print('#'*80)
print('Solution 2')
print('#'*80)
print(sol.permutation_stefan(l))
