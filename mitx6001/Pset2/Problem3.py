#!/usr/bin/env python3

def remainBalance(initBalance, annualInterestRate, monthlyPayment):
    balance = initBalance
    for i in range(12):
        unpaidBalance = balance - monthlyPayment
        interest = (annualInterestRate) / 12 * unpaidBalance
        balance = unpaidBalance + interest
    return balance

def bisection(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lo = balance / 12.0
    up = balance * (1 + monthlyInterestRate) ** 12 / 12.0
    while True:
        mid = (lo + up) / 2
        res = remainBalance(balance, annualInterestRate, mid)
        if res < -0.001:
            up = mid
        elif res > 0.001:
            lo = mid
        else:
            return mid

print("%.2f" % bisection(balance, annualInterestRate))
