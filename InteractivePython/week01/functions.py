#!/usr/bin/env python3

def triangle_area(base, height):
    area = (1.0 / 2) * base * height
    return area

a1 = triangle_area(3, 8)
print(a1)
a2 = triangle_area(2, 12)
print(a2)

def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9.0) * (fahrenheit - 32.0)
    return celsius

print(fahrenheit2celsius(32))
print(fahrenheit2celsius(212))

def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

print(fahrenheit2kelvin(32))
print(fahrenheit2kelvin(212))
