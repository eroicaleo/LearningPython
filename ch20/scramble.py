#!/usr/bin/python3.3

def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]
