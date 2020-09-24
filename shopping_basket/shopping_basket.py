class Basket:
    def __init__(self):
        self.sub_total = 0.0
        self.discount = 0.0
        self.total = 0.0
        self.items = []

    def add_item(self, name: str, price, quantity):
        if type(name) == str:
            self.items.append(name)
        else:
            raise TypeError

