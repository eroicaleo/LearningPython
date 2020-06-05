#!/usr/bin/env python3

class StockSpanner:

    def __init__(self):
        self.price_list = []
        self.span = []

    def next(self, price: int) -> int:
        ix, ret = len(self.price_list)-1, 1
        while ix >= 0 and self.price_list[ix] <= price:
            ret += self.span[ix]
            ix -= self.span[ix]
        self.price_list.append(price)
        self.span.append(ret)
        return ret

sp = StockSpanner()
price_list = [100, 80, 60, 70, 60, 75, 85]
for p in price_list:
    print(sp.next(p))
# [1,1,1,2,1,4,6]

