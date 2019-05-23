#!/usr/bin/env python3

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sort the array
        length, nums = len(nums), sorted(nums)
        # create a hash/set to filter out duplicate
        visited = set()
        ret = []
        print(nums)
        # 2-loops
        for i in range(0, length-3):
            for j in range(i+1, length-2):
                print(i, j, nums[i], nums[j])
                print(visited)
                # filter out duplicate
                if (nums[i], nums[j]) in visited:
                    continue
                else:
                    visited.add((nums[i], nums[j]))

                # use 2 points
                sum2 = target-nums[i]-nums[j]
                p, q = j+1, length-1
                while p < q:
                    if   nums[p] + nums[q] > sum2: q -= 1
                    elif nums[p] + nums[q] < sum2: p += 1
                    else:
                        ret.append([nums[i],nums[j],nums[p],nums[q]])
                        while p < q and nums[p] == nums[p+1]:
                            p += 1
                        p, q = p+1, q-1
                print(ret)
        return ret

nums = [1, 0, -1, 0, -2, 2]
target = 0
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9
sol = Solution()
print(sol.fourSum(nums, target))
