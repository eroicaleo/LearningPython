#!/usr/bin/env python

def divideNew(x, y):
    try:
        results = x / y
    except ZeroDivisionError, e:
        print 'Division by zero!' + str(e)
    except TypeError:
        divideNew(int(x), int(y))
    else:
        print 'result is', results
    finally:
        print 'executing finally clause!'

divideNew(3 , 4)
divideNew(3 , 0)
divideNew('3' , '4')

# mylist = [10, 20, 30] 
# mylist.index(11)

def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        FancyDivide(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    else:
        print "1"
    finally:
        print "0"

FancyDivide([0, 2, 4], 1)
FancyDivide([0, 2, 4], 4)
FancyDivide([0, 2, 4], 0)

def FancyDivide(numbers,index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    except ZeroDivisionError, e:
        print "-2"

FancyDivide([0, 2, 4], 1)
FancyDivide([0, 2, 4], 4)
FancyDivide([0, 2, 4], 0)

def FancyDivide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e

FancyDivide([0, 2, 4], 0)
