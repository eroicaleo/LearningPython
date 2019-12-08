#!/usr/bin/env python3

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        num1 = [int(s) for s in version1.split('.')]
        num2 = [int(s) for s in version2.split('.')]
        len1, len2 = len(num1), len(num2)
        if len1 > len2:
            num2 += [0] * (len1 - len2)
        elif len2 > len1:
            num1 += [0] * (len2 - len1)
        for d1, d2 in zip(num1, num2):
            if d1 < d2:
                return -1
            elif d1 > d2:
                return 1
        return 0

version1 = "1.0"
version2 = "1.0.0"
version1 = "1.01"
version2 = "1.001"
version1 = "7.5.2.4"
version2 = "7.5.3"
version1 = "1.0.1"
version2 = "1"
version1 = "0.1"
version2 = "1.1"
sol = Solution()
print(sol.compareVersion(version1, version2))
print([0]*-1)
