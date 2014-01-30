#!/usr/local/bin/python3.3

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for arg in args[1:]:
            if x not in arg:
                break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for arg in args:
        for x in arg:
            if x not in res:
                res.append(x)
    return res

print(intersect("SPAM", "SCAM", "SLAM"))
print(union("SPAM", "SCAM", "SLAM"))

def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(*items)
        print(sorted(func(*items)))
    return

tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)
