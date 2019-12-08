#!/usr/bin/env python3

class Solution:
    def fizzBuzz(self, n: int):
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append('{i}'.format(i=i))
        return res

sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(15))
print(sol.fizzBuzz(1))
print(sol.fizzBuzz(0))
