#!/usr/local/bin/python3.3

if 1:
    print(True)


if not 1:
    print(True)
else:
    print(False)

x = 'killer rabbit'
if x == 'roger':
    print('shave and a hair cut')
elif x == 'bug':
    print("what's up doc?")
else:
    print('Run away!')

choice = 'ham'
branch = {'spam': 1.25,
        'ham' : 1.99,
        'eggs': 0.99,
        'bacon': 1.10
        }
print(branch[choice])

if choice == 'ham':
    print(1.99)
elif choice == 'spam':
    print(1.25)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad Choce')

branch = {'spam': 1.25,
        'ham' : 1.99,
        'eggs': 0.99,
        }

print(branch.get('ham', 'Bad Choice'))
print(branch.get('bacon', 'Bad Choice'))

choice = 'bacon'
print("Using in statement")
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

print("Using try - except")
try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

L = [
        'good',
        'bad',
        'ugly'
    ]

print(L)

print((2 or 3, 3 or 2))

print(() or {})

print("###### tenary expression:")
A = 't' if 'spam' else 'f'
print(A)

A = 't' if '' else 'f'
print(A)

print(['f', 't'][bool('')])
print(['f', 't'][bool('spam')])

L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L)))

print(L)
print([x for x in L if x])
print(any(L))
print(all(L))
