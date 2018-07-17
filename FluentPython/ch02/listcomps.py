#!/usr/bin/env python

symbols = '$¢£¥€¤'
codes = [ord(code) for code in symbols]
print(codes)

beyond_ascii = [ord(code) for code in symbols if ord(code) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
