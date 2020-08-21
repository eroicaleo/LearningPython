#!/usr/bin/env python

class Solution:
    def carFleet(self, target, position, speed): 
        pair = sorted(zip(position, speed), reverse=True)
        ret = curr_time = 0
        for p, v in pair:
            t = (target-p)/v
            if t > curr_time:
                ret, curr_time = ret+1, t
        return ret
            
target = 10
position = [0,4,2]
speed = [2,1,3]

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

sol = Solution()
print(sol.carFleet(target, position, speed))
