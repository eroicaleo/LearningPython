#!/usr/bin/env python3

# This is the thinking process: “Java/Python easy Solution with explanation”
# if n > m, then we can find one left-most bit i, such that n[i] = 1, m[i] = 0
# For any j > i, m[j] = n[j]
# Then 

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        r, d, k = 0, 1, m
        for i in range(31):
            print(f'd = {d}, k = {k}, n = {n}, (k+1)*d = {(k+1)*d}')
            if k == 0:
                break
            r += ((k+1)*d > n and (k%2)) * d
            d, k = d*2, k//2
        return r

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        i = 1
        while n > m:
            m, n, i = m//2, n//2, i*2
        return n*i

sol = Solution()
print(sol.rangeBitwiseAnd2(2**31-2, 2**31-1))
print(sol.rangeBitwiseAnd2(6, 7))
print(sol.rangeBitwiseAnd2(2**31-1, 2**31-1))
print(sol.rangeBitwiseAnd2(0, 1))
print(sol.rangeBitwiseAnd3(5, 7))
