#!/usr/bin/env python3

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = [list(map(int, n)) for n in (num1, num2)]
        len1, len2 = len(l1), len(l2)
        lenm, lenn = (len(l1)+len(l2)+1), (len(l1)+1)
        m = [0] * lenm
        for i in range(0, len2):
            n, d2 = [0]* lenn, l2[len2-1-i]
            sum1 = add1 = 0
            for j in range(len(l1)-1,-1,-1):
                s = l1[j]*d2+add1
                sum1, add1 = s%10, s//10
                n[j+1] = sum1
            n[0] = add1
            sum1 = add1 = 0
            for j in range(len(n)-1,-1,-1):
                ix = (len(m)-1)-(len(n)-1-j)-i
                s = m[ix]+n[j]+add1
                m[ix], add1 = s%10, s//10

            print(d2, list(l1), n, m)
        return ''.join(map(str, m)).lstrip('0')

sol = Solution()
num1, num2 = '123', '456'
num1, num2 = '123', '1'
num1, num2 = '123', '0'
num1, num2 = '408', '5'
print(sol.multiply(num1, num2))
print(list(range(4,-1,-1)))
