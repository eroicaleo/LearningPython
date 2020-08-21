#!/usr/bin/env python

class Solution:
    def toGoatLatin(self, S):
        return ' '.join([(w if w[0] in 'aeiou' else w[1:]+w[0])+'ma'+'a'*(i+1) for i, w in enumerate(S.split())])

S = 'I speak Goat Latin'
S = 'The quick brown fox jumped over the lazy dog'
sol = Solution()
print(sol.toGoatLatin(S))
