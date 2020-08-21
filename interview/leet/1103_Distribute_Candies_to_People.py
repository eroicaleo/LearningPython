#!/usr/bin/env python

class Solution:
    def distributeCandies(self, candies, num_people):
        offset, ret = 0, [0]*num_people
        while sum(range(offset+1, offset+num_people+1)) <= candies:
            ret = [i+j+offset for i, j in zip(ret, range(1,num_people+1))]
            candies -= sum(range(offset+1, offset+num_people+1))
            offset += num_people
        print(ret, candies)
        for i in range(1,num_people+1): 
            d = min(offset+i, candies)
            ret[i-1] += d
            candies -= d
            if candies == 0:
                break
        return ret

sol = Solution()
candies, num_people = 10, 3
candies, num_people = 7, 4
print(sol.distributeCandies(candies, num_people))
