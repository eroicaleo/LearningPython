#!/usr/bin/env python

class Solution:
    def hIndex(self, citations) -> int:
        length = len(citations)
        if length == 0:
            return 0
        hl, hh = 0, citations[-1]
        while hl < hh:
            hm = (hl+hh)//2
            # print(hl, hh, hm)
            if hm > length:
                hh = hm-1
            elif hm == 0 or citations[length-hm] >= hm: # h >= hm
                hl = hm+1
                if hl > length or citations[length-hl] < hl:
                    return hl-1
            elif citations[length-hm] < hm: # h < hm
                hh = hm-1
        return hl

citation_list = [
[100],
[0],
[],
[0, 1, 4, 5, 6],
[0, 1, 3, 5, 6],
[1,2],
[0, 0, 0],
[0, 1],
[0, 0, 4, 4],
[100,200],
]
sol = Solution()
for citations in citation_list:
    print(citations, sol.hIndex(citations))
