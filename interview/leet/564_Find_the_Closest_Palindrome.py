#!/usr/bin/env python

class Solution:
    def nearestPalindromic(self, n):
        mid = len(n) // 2
        if len(n) % 2 == 0:
            s1 = n[0:mid] + n[0:mid][::-1]
        else:
            s1 = n[0:mid+1] + n[0:mid][::-1]
        s2, s3, s2_list, s3_list = '0', '9'*len(n), list(s1), list(s1)
        # This is wrong, e.g. 230032, the smaller one should be 229932, not 220022
        # So needs to use awice's method
        for i in range(mid, len(n)):
            if s2_list[i] != '0':
                s2_list[len(n)-1-i] = s2_list[i] = chr(ord(s1[i])-1)
                s2 = ''.join(s2_list)
                if s2 == '0' * len(n) and len(n) > 1:
                    s2 = '9' * (len(n)-1)
                break
        for i in range(mid, len(n)):
            if s3_list[i] != '9':
                s3_list[len(n)-1-i] = s3_list[i] = chr(ord(s1[i])+1)
                s3 = ''.join(s3_list)
                break
        if s1 == '9' * len(n):
            s3 = '1' + '0'*(len(n)-1) + '1'
        slist = [s2, s1, s3] if s1 != n else [s2, s3]
        l = [max(abs(int(s)-int(n)), 1) for s in slist]
        return slist, l, slist[l.index(min(l))]

sol = Solution()
n = '123'
n = '81'
n = '21'
n = '10'
n = '1'
n = '22'
n = '99'
n = '9'
print(sol.nearestPalindromic(n))
