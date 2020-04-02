#!/usr/bin/env python3

class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        print(f'S = {S}')
        if len(S) <= 2:
            return S
        if S[:2] == '10':
            return self.makeLargestSpecial(S[2:]) + '10'
        hi, cnt = len(S)-1, 0
        for i, c in enumerate(S):
            cnt += 1 if c == '1' else -1
            if cnt == 0:
                print(f'cnt = {cnt}, i = {i}')
                break
        if i == hi:
            return '1' + self.makeLargestSpecial(S[1:hi]) + '0'
        return self.makeLargestSpecial(S[:i+1]) + self.makeLargestSpecial(S[i+1:])

S = "11011000"
S = '10'
S = ''
S = "11100010"
sol = Solution()
print(sol.makeLargestSpecial(S))
