class Basket:
    def __init__(self):
        self.sub_total = 0.0
        self.discount = 0.0
        self.total = 0.0
        self.items = []

    def add_item(self, *args):
        for i in args:
            quan = i.quantity
            n = i.name
            p = i.price
            if type(n) == str:
                for x in range(quan):
                    self.items.append(n)
                    self.sub_total += p
                    print(self.sub_total)
            else:
                raise TypeError
        

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Pricer:
    def __init__(self, obj):
        return
