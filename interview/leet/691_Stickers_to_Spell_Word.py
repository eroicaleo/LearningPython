#!/usr/bin/env python3

# 'thehat' -> {h:2, t:2, e:1, a:1}
# 'with' -> {t:1, h:1}
# 'example' -> {e:2, a:1}
# 'science' -> {e:2}

#                           e:1 a:1 h:2 t:2    
# 'with'    -> {t:1, h:1}   inf inf 2   2
# 'example' -> {e:2, a:1}   1   1   3
# 'science' -> {e:2}

#      th  eae ee
# e:1  inf 1   1
# a:1  inf 1   inf
# h:2  2   inf inf
# t:2  2   inf inf

#       th          eae          ee
#   th  ea,2        thth         ththa

from collections import Counter
class Solution:
    def minStickers(self, stickers, target):
        stickers = set([''.join(sorted([c for c in w if c in target])) for w in stickers])
        def isSubset(s, t):
            return Counter(s)-Counter(t)=={}
        stickers = [s for s in stickers if not any(isSubset(s, t) for t in stickers if s != t)]
        c_stickers = [Counter(s) for s in stickers]
        print(c_stickers)
        self.ret = float('inf')
        self.d = {}
        def dfs(left):
            if left == "":
                return 0
            if left in self.d:
                return self.d[left]
            r = []
            for w in stickers:
                if set(w) & set(left):
                    lc = Counter(left) - Counter(w)
                    l = ''.join(lc[k]*k for k in sorted(lc))
                    r.append(1+dfs(l))
                else:
                    r.append(float('inf'))
            print(f'left = {left}, r = {r}')
            self.d[left] = min(r)
            return self.d[left]
        dfs(target)
        return -1 if self.d[target] == float('inf') else self.d[target]

stickers, target = ['with', 'example', 'science'], 'thehat'
stickers, target = ['notice', 'possible'], 'basicbasic'
sol = Solution()
print(sol.minStickers(stickers, target))
# print(Counter({'a':1})-Counter({'b':1, 'a':1})=={})
