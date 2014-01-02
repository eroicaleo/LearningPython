#!/usr/local/bin/python3.3

while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(int(reply) ** 2)
print("Good bye!")
