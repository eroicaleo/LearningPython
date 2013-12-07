#!/usr/local/bin/python3.3

import sys

S = 'aa$bb$cc$dd'
S = S.replace('$', 'SPAM')
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM');
print(where)
S = S[:where] + 'EGG' + S[where+len('SPAM'):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
S = S.replace('SPAM', 'EGG')
print(S)
S = S.replace('EGG', 'SPAM', 2)
print(S)

S = 'spammmy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'x'
L[5] = 'x'
print(L)
S = ''.join(L)
print(S)

S = 'SPAM'.join(['eggs', 'sausages', 'hams', 'toasts'])
print(S)

line = 'aaa bbb    ccc'
cols = line.split()
print(cols)

line = 'bob,hacker,40'
cols = line.split(',')
print(cols)

line = 'ISPAMamSPAMaSPAMlumberjack'
cols = line.split('SPAM')
print(cols)

line = 'The knight who says Hi!\n'
print(line)
print(line.rstrip())
print(line.upper())
print(line.lower())
print(line.isalpha())
print(line.endswith('Hi!\n'))
print(line.startswith('The'))
print(line.find('Hi') != -1)
print('Hi' in line)
sub = 'Hi!\n'
print(sub in line)
print(line.endswith(line[-len(sub):]))

exclaimation = 'Ni!'
print('The knights who say %s\n' % exclaimation)
print('%d %s %g you' % (1, 'spam', 4))

x = 1234
res = "integers:....%d....%-6d....%06d" % (1234, 1234, 1234)
print(res)
res = (1234,) * 4
res = "integers:....%d....%-6d....%06d...%6d" % res
print(res)

print("%f, %.2f, %.*f" % (1/3.0, 1/3.0, 4, 1/3.0))

print("%(qty)s more %(food)s" % {'qty': 1, 'food': 'spam'})

reply = """
Greetings %(name)s,
Your age is %(age)s!
Best,
Yang
""" % ({'name': 'Bob', 'age': 40})

print(reply)

qty = 10
food = 'spam'
print("%(qty)s more %(food)s" % vars())

template = '{0}, {1} and {2}'
print(template)
print(template.format('spam', 'ham', 'eggs'))
template = '{motto}, {pork} and {food}'
print(template.format(motto='spam', pork='ham', food='eggs'))
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))

print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

somelist = list('SPAM')
print(somelist)
print('first = {0[0]}, third = {0[2]}'.format(somelist))
print('first = {0}, third = {1}'.format(somelist[0], somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]
print('first = {0}, second = {2}, third = {1}'.format(*parts))
print('first = {0}, second = {2}, third = {1}, number = {3}'.format(parts[0], parts[1], parts[2], 1234))

print('{0:10} = {1:10}'.format('spam', 123.4567));
print('{0:>10} = {1:<10}'.format('spam', 123.4567));
print('"{0.platform:>10} = {1[kind]:<10}"'.format(sys, dict(kind='laptop')))

print('"{0:d}, {0:x}, {0:o}, {0:b}"'.format(255, 255, 255, 255))
print(0o377, 0xFF, 0b11111111)
print(0b11111111, bin(255), int('11111111', 2))
print(0o377, oct(255), int('377', 8))
print(0xFF, hex(255), int('FF', 16))

print("%.*f" % (4, 1/3.0))
print("{0:.{1}f}".format(1/3.0, 4))

# from formats import commas
print("{:,d}".format(999999999))
print("".join(["{:,d}".format(x) for x in (888888888, 999999999)]))
