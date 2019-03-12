#!/usr/bin/env python

class Solution:
    def getSkyline(self, buildings):
        from heapq import heappush, heappop
        heaphi, ret, currhi, xcord, i, buildings = [(0, -float('inf'), -1)], [], 0, 0, 0, buildings+[[float('inf'), float('inf'), 0]]
        while i+1 < len(buildings) or len(heaphi) > 1:
            print('i, b = ', i, buildings[i])
            xcord = min(-heaphi[0][1], buildings[i][0])
            if -heaphi[0][1] < buildings[i][0]:
                while (-heaphi[0][1] <= xcord) or (heaphi[0][0] == -currhi):
                    heappop(heaphi)
                    print('after  pop , heaphi =', heaphi)
                currhi, ret = -heaphi[0][0], ret + [[xcord, -heaphi[0][0]]]
                print('after  pop , currhi =', currhi)
            prevhi = currhi
            while i+1 < len(buildings) and buildings[i][0] == xcord:
                b, i = buildings[i], i+1
                print('b, xcord: ', b, xcord)
                currhi = max(currhi, b[2])
                heappush(heaphi, (-b[2], -b[1], i))
            if currhi > prevhi:
                ret.append([xcord, currhi])
            print('after  push, heaphi =', heaphi)
            print('after  push, currhi =', currhi)
        return ret

buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
buildings = [ [2, 3, 10],  [2, 4, 15], [2, 5, 20] ]
buildings = [ [2, 3, 10],  [3, 4, 10], [4, 5, 10] ]
buildings = []
sol = Solution()
print(sol.getSkyline(buildings))

