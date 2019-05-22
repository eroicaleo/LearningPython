#!/usr/bin/env python3

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        nrow, ncol = len(matrix), len(matrix[0])
        height = [0] * (ncol+1)
        maxArea = 0
        for row in matrix:
            for i in range(ncol):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
            print(height)

            stack = []
            for i, h in enumerate(height):
                print(i, h)
                print('stack before:', stack)
                while stack and height[stack[-1]] > h:
                    top = stack.pop()
                    left = (stack[-1] if stack else -1)
                    maxArea = max(maxArea, height[top]*(i-1-left))
                stack += [i]
                print('stack after:', stack)
                print('maxArea:', maxArea)

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
matrix = [
        ["1","0","1","1","0","1"],
        ["1","1","1","1","1","1"],
        ["0","1","1","0","1","1"],
        ["1","1","1","0","1","0"],
        ["0","1","1","1","1","1"],
        ["1","1","0","1","1","1"]
]
sol = Solution()
sol.maximalRectangle(matrix)
