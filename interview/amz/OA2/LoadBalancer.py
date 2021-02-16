#!/usr/bin/env python

class Solution:
    def loadBalancer(self, arr):
        p0, p1 = [0]*len(arr), [0]*len(arr)
        s, l = 0, len(arr)
        for i, n in enumerate(arr):
            p0[i] = s = s+n
        s = 0
        for i in range(l-1,-1,-1):
            p1[i] = s = s+arr[i]
        i, j = 0, l-1
        while i+1 < j-1:
            rest = (p1[0]-p0[i]-p1[j]-arr[i+1]-arr[j-1])
            print(i, j, p0[i], p1[j], rest)
            if p0[i] == p1[j] == rest:
                return True
            if p0[i] <= p1[j]:
                i += 1
            else:
                j -= 1
        return False

arr = [2,4,5,3,3,9,2,2,2]
arr = [1,1,1,1]
sol = Solution()
print(sol.loadBalancer(arr))
