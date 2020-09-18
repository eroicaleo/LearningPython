#!/usr/bin/env python3

class Solution:

    # This is O2 Solution
    def find132pattern(self, nums):
        stack, inc = [nums[0]], -1
        for n in nums[1:]:
            for j in range(0,len(stack)-1,2):
                if stack[j] < n < stack[j+1]:
                    return True
            if inc * (stack[-1]-n) > 0:
                inc = -inc
            else:
                stack.pop()
            stack.append(n)
        return False

    # This is O(n) Solution
    def find132pattern_O1(self, nums):
        l, arr = len(nums), list(nums)
        for i in range(1, l):
            arr[i] = min(arr[i-1], nums[i-1])

        stack = []
        for j in range(l-1,-1,-1):
            if nums[j] > arr[j]:
                while stack and stack[-1] <= arr[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                else:
                    stack.append(nums[j])
        return False

    # This is O(n) Solution, one pass
    # The idea is to keep track the max value of all possible
    # 3rd no. so far
    # a number can be 3rd no. when there is another no. coming before
    # and greater than it.

    # For current element, check if it can be the first element
    # If yes, we can return 
    # If not, it means it's >= 3rd, it can be the 2nd
    # We use this current element to update 3rd.
    # More specifically, we pop all element in the stack that is smaller
    # than current element, these elements can be the 3rd
    # Note that stack is still sorted, top is the smallest element.
    def find132pattern_O1_1pass(self, nums):
        third, stack = float('-inf'), []
        for n in reversed(nums):
            if n < third:
                return True
            while stack and stack[-1] < n:
                third = stack.pop()
            stack.append(n)
        return False


nums_list = [
[1,2,3,4],
[3,1,4,2],
[-1,3,2,0],
[1,2,3,-4,-3],
[1,2,3,-4,-3,-2,-3],
]
sol = Solution()
for nums in nums_list:
    print(nums, sol.find132pattern_O1(nums))
    print(nums, sol.find132pattern_O1_1pass(nums))
