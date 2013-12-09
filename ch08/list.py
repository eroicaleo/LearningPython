#!/usr/local/bin/python3.3

L = [1, 2, 3]
print(L)
print("Then length of L is %d" % len(L))
L = [1, 2, 3] + [4, 5, 6]
print("Now L is %s" % L)

L = ["Ni!"] * 4
print(L)

L = [1, 2]
L = str(L) + "34"
print(L)
L = [1, 2]
L = L + list("34")
print(L)

print(3 in [1, 2, 3])
for x in [1, 2, 3]:
  print(x, end=" ")
print();

res = "SPAM"
L = [x * 4 for x in res]
print(L)

L = list(map(abs, range(-2, 3)))
print(L)

L = ["Spam", "spam", "SPAM!"]
print(L[-2])
print(L[1:])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
matrix = [[x, x+1, x+2] for x in (1, 4, 7)]
print(matrix)
matix = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(matrix)

L = [1]
L[:0] = [2, 3, 4]
print(L)
L[len(L):] = [5, 6, 7]
print(L)
L.extend([8, 9, 10])
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort()
print(L)
L.sort(key=str.lower)
print(L)
L.sort(key=str.lower, reverse=True)
print(L)

L = [1, 2]
M = L[:]
print(M)
M.append([3, 4, 5])
print(M)
K = L[:]
K.extend([3, 4, 5])
print(K)
K = L[:]
K.insert(0, [3, 4, 5])
print(K)

L = ['spam', 'eggs', 'ham']
print("The index of eggs is {0}".format(L.index('eggs')))
L.insert(1, 'toast')
print(L)
L.remove('eggs')
print(L)
L.pop(1)
print(L)
print("There is {} number of spam in the list".format(L.count("spam")))

L = ['spam', 'toast', 'eggs', 'ham']
del L[0]
print(L)
del L[1:]
print(L)


