#!/usr/bin/env python

    def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s

        rowDict = ['' for i in range(numRows)]
        i, incr = 0, 1
        for c in s:
            rowDict[i] += c
            if i == numRows - 1:
                incr = -1
            elif i == 0:
                incr = +1
            i += incr
        
        res = ''.join(rowDict)

        return res

print(convert("PAYPALISHIRING", 3))
