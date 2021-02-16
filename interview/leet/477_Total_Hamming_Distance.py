#!/usr/bin/env python3

class Solution:
    def totalHammingDistance(self, nums):
        l, ret = len(nums), 0
        for i in range(31):
            k = sum((n&(1<<i))>>i for n in nums)
            ret += k*(l-k)
        return ret

    def totalHammingDistance_Stefan(self, nums):
        m = map(lambda x: f'{x:032b}', nums)
        # z = zip(*m)
        return sum(b.count('0') * b.count('1') for b in zip(*(m)))

    def totalHammingDistance_awice(self, nums):
        l = len(nums)
        bit = [0]*32
        for n in nums:
            for i in range(32):
                bit[i] += n%2
                n //= 2
        return sum(b*(l-b) for b in bit)


sol = Solution()
nums = [4,14,2]
print(sol.totalHammingDistance(nums))
print(sol.totalHammingDistance_Stefan(nums))
print(sol.totalHammingDistance_awice(nums))

print(list(zip(*['100', '011'])))
print(*['100', '011'])
a, b = (*['100', '011'], )
print(f'a = {a}, b = {b}')
