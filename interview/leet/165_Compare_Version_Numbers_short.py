#!/usr/bin/env python3

import itertools

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # num1 = [int(s) for s in version1.split('.')]
        # num2 = [int(s) for s in version2.split('.')]
        # Can be shorten to the following
        v1, v2 = (list(map(int, v.split('.'))) for v in (version1, version2))

        # len1, len2 = len(num1), len(num2)
        # if len1 > len2:
        #     num2 += [0] * (len1 - len2)
        # elif len2 > len1:
        #     num1 += [0] * (len2 - len1)
        # Can be shorten to the following

        # d = len(v1) - len(v2)
        # v1, v2 = v1+[0]*d, v2+[0]*-d
        v1, v2 = zip(*itertools.zip_longest(v1, v2, fillvalue = 0))
        print(v1, v2)

        # for d1, d2 in zip(num1, num2):
        #     if d1 < d2:
        #         return -1
        #     elif d1 > d2:
        #         return 1
        # return 0
        return (v1>v2)-(v1<v2)

version1 = "1.0.1"
version2 = "1"
version1 = "0.1"
version2 = "1.1"
version1 = "1.01"
version2 = "1.001"
version1 = "7.5.2.4"
version2 = "7.5.3"
version1 = "1.0"
version2 = "1.0.0"
sol = Solution()
print(sol.compareVersion(version1, version2))

