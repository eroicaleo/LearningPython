#!/usr/bin/env python

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        import random
        def partition(lo, hi):
            i, j = lo+1, hi
            while True:
                while i <= hi and nums[i] > nums[lo]: i += 1
                while j >= lo and nums[j] < nums[lo]: j -= 1
                if j <= i: break
                nums[i], nums[j], i, j = nums[j], nums[i], i+1, j-1
            nums[lo], nums[j] = nums[j], nums[lo]
            print("partition: ", lo, hi, j)
            return j
        def suffle():
            l = len(nums)
            for i in range(l):
                r = random.randrange(i, l)
                nums[i], nums[r] = nums[r], nums[i]
        lo, hi, k, _ = 0, len(nums)-1, k-1, suffle()
        while lo < hi:
            j = partition(lo, hi)
            if j == k: return nums[k]
            elif j > k: hi = j - 1
            elif j < k: lo = j + 1
        return nums[lo]

sol = Solution()
nums, k = [3,2,3,1,2,4,5,5,6], 4
nums, k = [3,2,1,5,6,4], 2
nums, k = [3,3,3,3,3,3,3,3,3], 1
print(sol.findKthLargest(nums, k))
