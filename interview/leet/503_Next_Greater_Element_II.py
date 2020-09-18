#!/usr/bin/env python3

class Solution:
    def nextGreaterElements(self, nums):
        if len(nums) == 0:
            return []
        l, stack = len(nums), []
        ret, i, head = [-1]*l, 0, -1
        while True:
            while stack and stack[-1][0] < nums[i]:
                ret[stack.pop()[1]] = nums[i]
            if head == i:
                break
            stack.append((nums[i], i))
            if len(stack) == 1:
                head = i
            i = (i+1)%l
        for _, i in stack:
            ret[i] = -1
        return ret

    # We check from the last element first
    # pick the last element, and goes from
    # the first element, until it reaches
    # one element that's greater than it.
    # then pick the second last element,
    # goes from the beginning.
    def nextGreaterElements_2(self, nums):
        n = len(nums)
        ret = [-1]*n
        stack = nums[::-1]
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            stack.append(nums[i])
        return ret

    # Lee215's solution is similar to mine
    # but easier to code
    def nextGreaterElements_lee215(self, nums):
        stack, res = [], [-1]*len(nums)
        for i in range(len(A)) * 2:
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res


num_list = [
[1,2,1],
[5,5,5,5,5],
[],
]
sol = Solution()
for nums in num_list:
    print(sol.nextGreaterElements(nums))
