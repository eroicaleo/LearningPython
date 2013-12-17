#!/usr/local/bin/python3.3

myfile = open('myfile.txt', 'w')
print(myfile.write('Hello world!\n'))
print(myfile.write('Goodbye text file!\n'))
myfile.close()

myfile = open('myfile.txt', 'r')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
myfile.close()

print(open('myfile.txt', 'r').read())

for line in open('myfile.txt', 'r'):
    print(line)


data = b'\x00\x00\x00\x07spam\x00\x08'
print(data)

open('data.bin', 'wb').write(data)

data = open('data.bin', 'rb').read()
print(data[4:8])
print(data[4:8][0])
print(bin(data[4:8][0]))
