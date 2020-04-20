#!/usr/bin/env python3

class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        self.ix, l = 0, len(S)
        def dfs():
            tokens = []
            while self.ix < l:
                c, self.ix = S[self.ix], self.ix+1
                if c == '1':
                    tokens.append(f'1{dfs()}0')
                else:
                    break
            return ''.join(sorted(tokens, reverse=True))
        return dfs()

S = "11100010"
S = "111000111100001100"
S = '1100'
S = '1010'
S = '10'
S = "11011000"
S = ''
sol = Solution()
print(sol.makeLargestSpecial(S))
