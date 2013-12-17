#!/usr/local/bin/python3.3

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write("%s,%s,%s\n" % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('datafile.txt', 'r').read()
print(chars)

F = open('datafile.txt', 'r')
line = F.readline()
line = line.rstrip()
print(line)

line = F.readline()
parts = line.split(',')
print(parts)
numbers = [int(P) for P in parts]
print(numbers)

line = F.readline()
parts = line.split('$')
print(parts)

print(eval(parts[0]))
print(eval(parts[1]))
objects = [eval(P) for P in parts]
print(objects)
