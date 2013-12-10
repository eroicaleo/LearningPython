#!/usr/local/bin/python3.3

keyslist = ['name', 'age']
valueslist = ['Bob', 40]

D = dict.fromkeys(keyslist)
print(D)
D = dict(zip(keyslist, valueslist))
print(D)
print(D.keys())

D = {'spam': 3, 'eggs': 1, 'ham': 2}
print(D)
print('The value of \'spam\' in D is {[spam]}'.format(D))
print(D['spam'])

# This is Illegal
"""
print('The value of \'spam\' in D is {['spam']}'.format(D))
print(D[spam])
"""

D = {'spam': 3, 'eggs': 1, 'ham': 2}
print(len(D))
print('spam' in D)
print(D.keys())
print(list(D.keys()))

D['ham'] = ['grill', 'bake', 'fry']
print(D)

del D['eggs']
print(D)
D['brunch'] = 'bacon'
print(D)

D = {'spam': 3, 'eggs': 1, 'ham': 2}
print(list(D.values()))
print(list(D.items()))

print(D.get('spam'))
print(D.get('toast'))
print(D.get('toast', 88))

D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)
print(D.pop('toast'))
print(D)
print(D.pop('muffin'))
print(D)

L = ['aa', 'bb', 'cc', 'dd']
print(L)
print(L.pop())
print(L)
print(L.pop(1))
print(L)

table = {
        '1975': 'Holy Grail',
        '1979': 'Life of Brian', 
        '1983': 'The Meaning of Life'
        }
year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])

table = {
        'Holy Grail': '1975',
        'Life of Brian': '1979',
        'The Meaning of Life': '1983'
        }
movie = 'Holy Grail'
year = table[movie]
print(year)

print(list(table.items()))

L = [title for (title, year) in table.items() if year == "1975"]
print(L)

# Using dictionaries to simulate flexible list
D = {}
D[99] = 'spam'
print(D)

table = {
        1975: 'Holy Grail',
        1979: 'Life of Brian', 
        1983: 'The Meaning of Life'
        }

print(list(table.items()))

# Using dictionaries to for sparse data structures: Tuple keys
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
print(Matrix)

if (2, 3, 6) in Matrix:
    print(Matrix[(2, 3, 6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)

print(Matrix.get((2, 3, 6), 1))

D = dict([('name', 'Bob'), ('age', '40')])
print(D)

# Dictionary changes in Python 3.3 and 2.7
print(list(zip([1, 2 ,3], ['a', 'b', 'c'])))
print(dict(zip([1, 2 ,3], ['a', 'b', 'c'])))

D = {k: v for (k, v) in zip([1, 2 ,3], ['a', 'b', 'c'])}
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

# Dictionary views
D = {'a': 1}
print(list(D.items()))
print(D.items() | D.keys())
print(D.items() | D)
print(D.items() | {('c', 3), ('d', 4)})
print(dict(D.items() | {('c', 3), ('d', 4)}))

# sorting

D = {'a': 1, 'c': 2, 'b': 3}
for k in sorted(D):
    print(k, D[k])

