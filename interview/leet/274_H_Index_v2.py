#!/usr/bin/env python3

class Solution:
    def hIndex(self, citations):
        for i, cite in enumerate(sorted(citations, reverse=True)):
            if cite <= i+1:
                # At this point, we know
                # 1. there are "cite" papers whose score >= cite
                # 2. there are i papers whose score >= i
                # 3. If i > cite, it's impossible for (i+1) papers whose score >= i+1
                #    because citations[i] = cite < i < i+1
                return max(i, cite)
        return len(citations)

    def hIndex_1line(self, citations):
        return sum(cite > i for i, cite in enumerate(sorted(citations, reverse=True)))

citation_list = [
[3,0,6,1,5],
[1,1,1,1,1],
[0,0,0,0,0],
[1,1,1,1,2],
[5,6,7],
[100,99,3,2,1],
[100,99,4,2,1],
[100,99,98,2,1],
]
sol = Solution()
for citations in citation_list:
    print(citations, sol.hIndex(citations))
for citations in citation_list:
    print(citations, sol.hIndex_1line(citations))
