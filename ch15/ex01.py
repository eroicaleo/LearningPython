#!/usr/local/bin/python3.3

S = 'hellomellon'
for c in S:
    print(c, ord(c))

print(sum([ord(c) for c in S]))
print([ord(c) for c in S])
print(list(map(ord, S)))
