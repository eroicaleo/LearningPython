#!/usr/bin/env python

from employees import PizzaRobot, Sever

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, sever):
        print(self.name, "orders from", sever)
    def pay(self, sever):
        print(self.name, "pays for item to", sever)

class Oven:
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.sever = Sever('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.sever)
        self.chef.work();
        self.oven.bake();
        customer.pay(self.sever)

if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
