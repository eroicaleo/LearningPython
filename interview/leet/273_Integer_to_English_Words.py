#!/usr/bin/env python

class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
                1 : 'One',
                2 : 'Two',
                3 : 'Three',
                4 : 'Four',
                5 : 'Five',
                6 : 'Six',
                7 : 'Seven',
                8 : 'Eight',
                9 : 'Nine',
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen',
                20: 'Twenty',
                30: 'Thirty',
                40: 'Fourty',
                50: 'Fifty',
                60: 'Sixty',
                70: 'Seventy',
                80: 'Eighty',
                90: 'Ninty',
                100: 'One Hundred',
                200: 'Two Hundred',
                300: 'Three Hundred',
                400: 'Four Hundred',
                500: 'Five Hundred',
                600: 'Six Hundred',
                700: 'Seven Hundred',
                800: 'Eight Hundred',
                900: 'Nine Hundred',
                1000: 'Thousand',
                1000000: 'Million',
                1000000000: 'Billion',
            }
        ret, divider = '', 1000000000
        if num == 0: return 'Zero'
        while divider >= 1:
            num, nextNum = num // divider, num % divider
            if num > 0:
                a = num - (num % 100)
                if a in d: ret += ' ' + d[a]
                b = (num-a)
                b = b if b in d else b - (b % 10)
                if b in d: ret += ' ' + d[b]
                c = num - a - b
                if c in d: ret += ' ' + d[c]
                if divider > 1: ret += ' ' + d[divider]
            num, divider = nextNum, divider // 1000
        return ret.strip()

sol = Solution()
i = 1234567891
i = 1234567
i = 0
i = 12345
print(i, sol.numberToWords(i))
