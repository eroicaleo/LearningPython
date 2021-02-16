#!/usr/bin/env python3

class Solution:
    def minDomino(self, A, B):
        num, A_list, B_list = [0]*7, [0]*7, [0]*7
        for i, d in enumerate(zip(A, B)):
            a, b = d
            num[a] += 1
            if a != b:
                num[b] += 1
                A_list[a] += 1
                B_list[b] += 1
            if num[a] == i+1:
                t = a
            elif num[b] == i+1:
                t = b
            else:
                return -1
        return min(A_list[t], B_list[t])

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
A = [3,5,1,2,3]
B = [3,6,3,3,4]
sol = Solution()
print(sol.minDomino(A, B))
