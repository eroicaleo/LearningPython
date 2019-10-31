#!/usr/bin/env python

errno = 50159747054
name = 'Bob'

print('Hello, %s there is a 0x%x error' % (name, errno))
str_ = 'Hello, %(name)s there is a 0x%(errno)x error' % {'name': name, 'errno': errno}
print('Dictionary in old style')
print(str_)

print('New style')
str_ = 'Hey {name}, there is a 0x{errno:x} error'.format(name=name, errno=errno)
print(str_)

print('Literal String Interpolation')
str_ = f'Hello, {name}!'
print(str_)

a, b = 5, 10
str_ = f'Five plus ten is {a+b}, not {2*(a+b)}'
print(str_)

def greet(name, question):
    return f'Hello, {name}! How is it {question}?'

print(greet('Bob', 'going'))

str_ = f'Hey {name}, there is a {errno:#x} error!'
print(str_)

print('Template')

from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)
print(t.substitute(name=name))
t = Template('Hey, $name! There is a $errno error!')
print(t.substitute(name=name, errno=hex(errno)))

SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        print('I am here')
        pass
err = Error()
user_input = '{error}.__init__()'
user_input = '{error.__init__.__globals__[SECRET]}'

# print(err.__init__.__globals__)

print(user_input.format(error=err))

user_input = Template('${error.__init__.__globals__[SECRET]}')
print(user_input.substitute(error=err))


