#!/usr/bin/env python3

class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        stack = []
        for c in S:
            if c == '1':
                stack.append(c)
            else:
                tokens = []
                while stack[-1] != '1':
                    tokens.append(stack.pop(-1))
                stack.append(stack.pop(-1)+''.join(sorted(tokens, reverse=True))+'0')
            print(f'c = {c}, stack = {stack}')
        return ''.join(sorted(stack, reverse=True))

S = "11100010"
S = "111000111100001100"
S = '1100'
S = '1010'
S = '10'
S = "11011000"
S = ''
S = "1011100010"
sol = Solution()
print(sol.makeLargestSpecial(S))
