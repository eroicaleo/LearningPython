#!/usr/bin/env python3

class Solution:
    def restoreIpAddresses(self, s: str):
        def restore(s, k):
            print(f'restore s={s}, k={k}')
            if len(s) > 3*k or len(s) == 0:
                return []
            if k == 1:
                if int(s) > 255 or (s[0] == '0' and s != '0'):
                    return []
                else:
                    return [s]
            ret = [s[0]+'.'+t for t in restore(s[1:], k-1)]
            if 10 <= int(s[:2]) <= 99:
                ret += [s[:2]+'.'+t for t in restore(s[2:], k-1)]
            if 100 <= int(s[:3]) <= 255:
                ret += [s[:3]+'.'+t for t in restore(s[3:], k-1)]
            return ret
        return restore(s, 4)


sol = Solution()
s = '25525511135'
s = '10000'
s = '100'
s = '00111'
s = '255255111353'
s = '11111'
s = '111111'
s = '00000'
s = '0000'
print(sol.restoreIpAddresses(s))
