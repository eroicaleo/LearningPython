#!/usr/bin/env python3

def isLeapYear(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False

year = 2012
leap_year = isLeapYear(year)
    
if leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
                    
