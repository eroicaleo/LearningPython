#!/usr/bin/env python3

from collections import Counter

class Solution:
    def majorityElement(self, nums):
        d, l = {}, len(nums)
        for n in nums:
            d[n] = d.get(n, 0) + 1
        return [k for k in d if d[k] > l//3]

    # When we reach 3 different numbers, we minus one
    # then we can minus at most l//3 times
    # So what left in counter might be a candidate for the majority element
    def majorityElement_Stefan(self, nums):
        ctr = Counter()
        for n in nums:
            ctr[n] += 1
            print(f'cnt is {ctr}')
            if len(ctr) == 3:
                ctr -= Counter(set(ctr))
                print(f'cnt becomes {ctr}')
        return [n for n in ctr if nums.count(n) > len(nums)//3]

    def majorityElement_vote(self, nums):
        d, l = {}, len(nums)
        for n in nums:
            if n in d or len(d) < 2:
                d[n] = d.get(n, 0)+1
            else:
                d = {k:d[k]-1 for k in d if d[k] > 1}
        return [n for n in d if nums.count(n) > len(nums)//3]



nums = [1,2,3,4,5]
nums = [3,2,3]
nums = [1,1,1,3,3,2,2,2]
sol = Solution()
print(sol.majorityElement(nums))
print(sol.majorityElement_Stefan(nums))
print(sol.majorityElement_vote(nums))
