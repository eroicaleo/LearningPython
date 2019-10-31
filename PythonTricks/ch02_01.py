#!/usr/bin/env python

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], "Wrong price"
    return price

apple = {'price': 1.99}
shoes = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(apple, 0.25))
# print(apply_discount(apple, -0.25))
print(apply_discount(shoes, 0.25))
# print(apply_discount(shoes, 2))

# assert 1==2, 'This should fail'
assert (1==2, 'This should fail')
