#!/usr/bin/env python3

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if ('.' in IP) and len(IP.split('.')) == 4:
            for x in IP.split('.'):
                if len(x) == 0 or not x.isdigit() or int(x) > 255 or (len(x) > 1 and x.startswith('0')):
                    return "Neither"
            return "IPv4"

        if (':' in IP) and len(IP.split(':')) == 8:
            for x in IP.split(':'):
                if len(x) == 0 or len(x) > 4:
                    return "Neither"
                for c in x:
                    if not (c.upper() in '0123456789ABCDEF'):
                        return "Neither"
            return "IPv6"

        return "Neither"

sol = Solution()
IP = "256.256.256.256"
IP = "172.16.254.1"
IP = "172.16.254.01"
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
IP = '02001:0db8:85a3:0000:0000:8a2e:0370:7334'
IP = '2001:0db8:85a3::8A2E:0370:7334'
IP = "1e1.4.5.6"
print(sol.validIPAddress(IP))
print(ord('9'))
print(ord('A'))
print(ord('a'))
