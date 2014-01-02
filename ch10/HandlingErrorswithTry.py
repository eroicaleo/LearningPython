#!/usr/local/bin/python3.3

while True:
    reply = input('Enter text: ')
    if reply == 'stop': 
        break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Good bye!')
