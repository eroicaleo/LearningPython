#!/usr/bin/env python

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[2])

for i in range(5):
    print(X[i], end=' ')
print()

L = [5, 6, 7, 8, 9]
print(L[:-1])
print(L[::2])

# explicitly use slice
print(L[slice(1, None)])
print(L[slice(None, -1)])
print(L[slice(None, None, 2)])

class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

X = Indexer()
print(X[2:4])
print(X[1:])
print(X[:-1])
print(X[::2])

class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing:', index)
        else:
            print('slicing:', index.start, index.stop, index.step)

X = Indexer()
X[99]
X[1:99:2]
X[1:]

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = 'Spam'
print(X[1])
for c in X:
    print(c, end=' ')
print()

print('p' in X)
print([c for c in X])
print(list(map(str.upper, X)))
print(list(X), tuple(X), ''.join(X))
