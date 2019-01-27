#!/usr/bin/env python

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1, sum2, lb = 0, 0, min(nums)
        mask1 = int('55555555', base=16)
        mask2 = int('AAAAAAAA', base=16)
        for num in nums:

            sum1 += ((num - lb) & mask1)
            sum2 += ((num - lb) & mask2) >> 1
            # print('before mod: ', num, bin(sum1)[2:], bin(sum2)[2:])

            for i in range(16):
                if (sum1 >> 2*i) & 3 == 3:
                    sum1 ^= (3 << 2*i)

                if (sum2 >> 2*i) & 3 == 3:
                    sum2 ^= (3 << 2*i)
            # print('after mod: ', num, bin(sum1)[2:], bin(sum2)[2:])
        
        return sum1 + (sum2 << 1) + lb

mask1 = int('55555555', base=16)
mask2 = int('AAAAAAAA', base=16)
nums1 = 2
int1 = (nums1 & mask1)
int2 = (nums1 & mask2) >> 1
nums = [0,1,0,1,0,1,99]
nums = [2,2,3,2]
nums = [2,2,5,5,1,5,1,1,0,2]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
print(int1)
print(int2)
sol = Solution()
print(sol.singleNumber(nums))

