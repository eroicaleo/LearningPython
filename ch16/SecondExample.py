#!/usr/local/bin/python3.3

def intersect(seq1, seq2):
    res = [x for x in seq1 if x in seq2]
    return res

S1 = "SPAM"
S2 = "SCAM"
print(intersect(S1, S2))
print(intersect([1, 2, 3], (1, 4)))

print('Try to get intersection of 1 and 2')
try: intersect(1, 2)
except:
    print("Got exceptions")
