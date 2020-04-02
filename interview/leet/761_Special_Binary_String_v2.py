#!/usr/bin/env python3

class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        self.ix = 0
        def dfs(S, level):
            tokens, sub_level_done = [], 0
            print(f'{"  "*level}before level = {level}, S = {S}, self.ix = {self.ix}, tokens = {tokens}')
            while self.ix < len(S):
                print(f'{"  "*level}while loop level = {level}, S = {S}, self.ix = {self.ix}, tokens = {tokens}')
                if S[self.ix] == '1':
                    print(f'{"  "*level}if clause loop level = {level}, S = {S}, self.ix = {self.ix}, tokens = {tokens}')
                    self.ix += 1
                    tokens.append(dfs(S, level+1))
                else:
                    print(f'{"  "*level}else clause loop level = {level}, S = {S}, self.ix = {self.ix}, tokens = {tokens}')
                    sub_level_done = 1
                    self.ix += 1
                    break
            ret = ''.join(sorted(tokens, reverse=True))
            if sub_level_done:
                ret = '1'+ret+'0'
            print(f'{"  "*level}after  level = {level}, S = {S}, self.ix = {self.ix}, tokens = {tokens}, ret = {ret}')
            return ret
        return dfs(S, 0)



S = ''
S = "11100010"
S = '10'
S = '1010'
S = '1100'
S = "11011000"
S = "111000111100001100"
sol = Solution()
print(sol.makeLargestSpecial(S))

