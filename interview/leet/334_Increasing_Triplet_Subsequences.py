#!/usr/bin/env python3

class Solution:
    def increasingTriplet(self, nums):
        triples = []
        for n in nums:
            if not triples:
                triples.append(n)
            elif n > triples[-1]:
                triples.append(n)
            elif n < triples[-1]:
                if len(triples) % 2 == 1:
                    triples[-1] = n
                elif len(triples) == 2 and triples[0] > n:
                    triples.append(n)
                elif len(triples) == 2 and triples[0] < n:
                    triples[-1] = n

            if len(triples) > 2 and triples[-1] > triples[1]:
                return True
            elif len(triples) == 4:
                triples = triples[2:]
        return False

num_list = [
[2,1,5,0,4,6],
[5,4,3,2,1],
[1,2,3,4,5],
[2,5,3,4,5],
]

sol = Solution()
for nums in num_list:
    print(nums, sol.increasingTriplet(nums))
