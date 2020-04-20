#!/usr/bin/env python3

class Solution:
    def circularArrayLoop(self, nums):
        l = len(nums)
        for i in range(l):
            print(f'i = {i}')
            head = slow = fast = i
            while True:
                slow  = (slow+nums[slow])%l
                fast1 = (fast+nums[fast])%l
                fast2 = (fast1+nums[fast1])%l
                if fast == fast1 or fast1 == fast2:
                    print(f'break 1 fast = nums[{fast}] = {nums[fast]}')
                    break
                if (nums[head]*nums[fast] <= 0) or (nums[head]*nums[fast1] <= 0):
                    print(f'break 2, fast = nums[{fast}] = {nums[fast]}')
                    break
                fast = fast2
                print(f'slow = nums[{slow}] = {nums[slow]}, fast = nums[{fast}] = {nums[fast]}')
                if slow == fast:
                    return True
            while head != fast:
                nums[head], head = 0, (head+nums[head])%l
            print(f'nums = {nums}')
        return False
                
sol = Solution()
nums = [-2, 1, -1, -2,-2]
nums = [2, -1, 1, 2,2]
nums = [-1, 2]
nums = [-1,-2,-3,-4,-5]
print(sol.circularArrayLoop(nums))
