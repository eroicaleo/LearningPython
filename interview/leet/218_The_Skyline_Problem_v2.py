#!/usr/bin/env python

class Solution:
    def getSkyline(self, buildings):
        from heapq import heappush, heappop
        heaphi, ret, currhi, xcord, i = [(0, -float('inf'), -1)], [], 0, 0, 0
        while buildings or (len(heaphi) > 1):
            if (buildings and (-heaphi[0][1] < buildings[0][0])) or (not buildings and len(heaphi) > 1): # pop from heap
                xcord = -heaphi[0][1]
                while (-heaphi[0][1] <= xcord) or (heaphi[0][0] == -currhi):
                    heappop(heaphi)
                    print('after  pop , heaphi =', heaphi)
                currhi = -heaphi[0][0]
                print('after  pop , currhi =', currhi)
                ret.append([xcord, currhi])
            elif buildings: # push to heap
                print('buildings:', buildings)
                xcord, prevhi = buildings[0][0], currhi
                # print('before push, heaphi =', heaphi)
                while buildings and buildings[0][0] == xcord:
                    b = buildings.pop(0)
                    heappush(heaphi, (-b[2], -b[1], i))
                    currhi, i = max(currhi, b[2]), i+1
                if currhi > prevhi:
                    ret.append([xcord, currhi])
                print('after  push, heaphi =', heaphi)
                print('after  push, currhi =', currhi)
        return ret

buildings = [ [2, 3, 10],  [3, 4, 10], [4, 5, 10] ]
buildings = [ [2, 3, 10],  [2, 4, 15], [2, 5, 20] ]
buildings = []
buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
sol = Solution()
print(sol.getSkyline(buildings))

