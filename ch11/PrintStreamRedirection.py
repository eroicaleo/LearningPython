#!/usr/local/bin/python3.3

print('Hello world!')

import sys
sys.stdout.write('Hello world!\n')

X = [1, 2, 3]
Y = [4, 5, 6]

print(X, Y)
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

open('log.txt', 'w')

temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print('spam')
print((1, 2, 3))
sys.stdout.close()
sys.stdout = temp
print('Back here')

log = open('log.txt', 'a')
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()

print(open('log.txt', 'r').read(), end='')

sys.stderr.write('Bad!' * 8 + '\n')
print('Bad!' * 8, file=sys.stderr)


print(open('log.txt', 'rb').read())

