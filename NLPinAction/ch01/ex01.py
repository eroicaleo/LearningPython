#!/usr/bin/env python3

import re

r = '(hello|hi|hey)[ ]*([a-z]*)'
print(re.match(r, 'Hello Rosa', flags=re.IGNORECASE))
print(re.match(r, 'hi ho, hi ho, it\'s off to work ...,', flags=re.IGNORECASE))
print(re.match(r, 'hey, what\'s up', flags=re.IGNORECASE))

re_greeting = re.compile(
        '''
        # All kinds of weird Greetings
        [^a-z]*
        (
            [y]o|
            ['h]?ello|
            ok|
            hey|
            (good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3})
        )

        # Seperator between greeting and name
        [\s,;:]{1,3}

        # Name
        ([a-z]{1,20})
        ''',
        flags=re.VERBOSE | re.IGNORECASE)

print(re_greeting.match('Hello Rosa'))
print(re_greeting.match('Hello Rosa').groups())
print(re_greeting.match('Good evening Rosa Parks').groups())
print(re_greeting.match('Good Morn\'n Rosa Parks'))
print(re_greeting.match('Yo Rosa'))

from collections import Counter
print(Counter("Guten Morgen Rosa".split()))
print(Counter("Good morning, Rosa!".split()))

my_names = set([
    'rosa',
    'rose',
    'chatty',
    'chatbot',
    'bot',
    'chatterbot',
    ])
curt_names = set([
    'hal',
    'you',
    'u',
    ])

# greeter_name = ''
# match = re_greeting.match(input())
# if match:
#     at_name = match.groups()[-1]
#     if at_name in curt_names:
#         print('Good one.')
#     elif at_name.lower() in my_names:
#        # print('Hi {}, How are you?'.format(greeter_name))
#         print(f'Hi {greeter_name}, How are you?')

