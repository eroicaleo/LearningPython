#!/usr/bin/python3.3

S1 = 'abc'
S2 = 'xyz123'
z = zip(S1, S2)
print(list(z))

print(list(zip([1, 2, 3], [2, 3, 4, 5])))

print(list(map(abs, [-2, -1, 0, 1, 2])))

print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))

print(list(map(lambda x, y: x+y, open('script2.py'), open('script2.py'))))

print([x+y for (x, y) in zip(open('script2.py'), open('script2.py'))])

def mymap(func, *seqs):
    res = []
    for x in zip(*seqs):
        res.append(func(*x))
    return res

print(list(mymap(abs, [-2, -1, 0, 1, 2])))

print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))

def mymap(func, *seqs):
    return [func(*x) for x in zip(*seqs)]

print(list(mymap(abs, [-2, -1, 0, 1, 2])))

print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))

def mymap(func, *seqs):
    return (func(*x) for x in zip(*seqs))

print(list(mymap(abs, [-2, -1, 0, 1, 2])))

print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))

def mymap(func, *seqs):
    for x in zip(*seqs):
        yield func(*x)

print(list(mymap(abs, [-2, -1, 0, 1, 2])))

print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))

def myzip(*seq):
    res = []
    seqs = [list(S) for S in seq]
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

print(list(myzip([1, 2, 3], [2, 3, 4, 5])))
print([x+y for (x, y) in zip(open('script2.py'), open('script2.py'))])

def mymappad(*seq, pad=None):
    res = []
    seqs = [list(S) for S in seq]
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

print(mymappad(S1, S2, pad=99))
print(mymappad(S1, S2))

def myzip(*seq):
    seqs = [list(S) for S in seq]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

print(list(myzip([1, 2, 3], [2, 3, 4, 5])))
print([x+y for (x, y) in myzip(open('script2.py'), open('script2.py'))])

def mymappad(*seq, pad=None):
    seqs = [list(S) for S in seq]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

print(list(mymappad(S1, S2, pad=99)))
print(list(mymappad(S1, S2)))

def myzip(*seq):
    minlen = min(len(S) for S in seq)
    return [tuple(S[i] for S in seq) for i in range(minlen)]

print(list(myzip([1, 2, 3], [2, 3, 4, 5])))

def mymappad(*seq, pad=None):
    maxlen = max(len(S) for S in seq)
    return [tuple(S[i] if i < len(S) else pad for S in seq) for i in range(maxlen)]

print(list(mymappad(S1, S2, pad=99)))
print(list(mymappad(S1, S2)))

def myzip(*seq):
    minlen = min(len(S) for S in seq)
    return (tuple(S[i] for S in seq) for i in range(minlen))

print(list(myzip([1, 2, 3], [2, 3, 4, 5])))

def myzip(*seq):
    iters = list(map(iter, seq))
    i = 0
    while iters:
        i = i+1
        print(i)
        res = [next(i) for i in iters]
        print(bool(iters))
        yield tuple(res)

print('lala')
print(list(myzip([1, 2, 3], [2, 3, 4, 5])))

