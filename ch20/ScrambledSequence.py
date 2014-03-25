#!/usr/bin/python3.3

L, S = [1, 2, 3], 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S)

# simple function
def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

print(scramble('spam'))     
print(scramble(L))

# generator function
def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

for x in scramble('spam'): 
    print(x)
for x in scramble(L): 
    print(x)

print(list(scramble('spam')))
print(list(scramble(L)))

# generator expression
S = 'spam'
G = (S[i:] + S[:i] for i in range(len(S)))
print(list(G))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(list(F('spam')))
print(list(F(L)))

for x in F(L):
    print(x, end=' ')
print()
