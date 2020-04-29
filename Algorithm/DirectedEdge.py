#!/usr/bin/env python3

class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def fromv(self):
        return self.v

    def to(self):
        return self.w

    def getVertex(self):
        return (self.v, self.w)

    def getWeight(self):
        return self.weight

    def __str__(self):
        return f'DirectedEdge, from: {self.fromv()}, to: {self.to()}, weight: {self.getWeight()}'

