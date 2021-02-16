#!/usr/bin/env python

import collections

class Solution:
    def countMisses(self, num, pages, maxCacheSize):
        cache, misses = collections.OrderedDict(), 0
        for n in pages:
            if n in cache:
                cache.move_to_end(n)
            else:
                misses += 1
                if len(cache) == maxCacheSize:
                    cache.popitem(last=False)
                cache[n] = n
            print(f'cache = {cache}')
        return misses

sol = Solution()
pages = [1,2,1,3,1,2]
maxCacheSize = 2
print(sol.countMisses(len(pages), pages, maxCacheSize))
