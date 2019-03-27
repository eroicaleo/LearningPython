#!/usr/bin/env python

class Solution:
    def letterCombinations(self, digits):
        phone_dict = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', }
        def backtracking(nums):
            if len(nums) == 1:
                return list(phone_dict[nums[0]])
            elif not nums:
                return []
            ret = []
            for s in backtracking(nums[1:]):
                for c in phone_dict[nums[0]]:
                    ret.append(c+s)
            return ret
        return backtracking(digits)

sol = Solution()
print(sol.letterCombinations('23'))
