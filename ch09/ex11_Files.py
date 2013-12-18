#!/usr/local/bin/python3.3

myfile = open('myfile.txt', 'w')
myfile.write('Hello file world!\n')
myfile.close()

for line in open('myfile.txt', 'r'):
    print(line)
