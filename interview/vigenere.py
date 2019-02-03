#!/usr/bin/env python

def decode(encrypted, key):
    tmp = ord(encrypted) - ord(key)
    if tmp < 0: tmp += 26
    return chr(ord('A') + tmp)

puzzle = 'GXUZQEPFQVJFGB MI EVTWK XE VZJAH XXCA HIMLUL QS EFKXNMJN CMVNGKORV'
puzzle_nospace = puzzle.replace(' ', '')
key = 'EQUIFAX' 
key_str = (key * (len(puzzle_nospace) // len(key) + 1))[0:len(puzzle_nospace)] 
ans = ''.join(map(decode, puzzle_nospace, key_str))
print(ans)
