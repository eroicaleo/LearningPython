#!/usr/bin/env python3

# 463. Island Perimeter

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution:
    def islandPerimeter(self, grid) -> int:
        nr, nc = len(grid), len(grid[0])
        p = 0
        for i in range(nr):
            last = 0
            for c in grid[i]+[0]:
                if c != last:
                    p += 1
                last = c
        for j in range(nc):
            last = 0
            for i in range(nr):
                if grid[i][j] != last:
                    p += 1
                last = grid[i][j]
            p += (last == 1)
        return p

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

sol = Solution()
print(sol.islandPerimeter(grid))
