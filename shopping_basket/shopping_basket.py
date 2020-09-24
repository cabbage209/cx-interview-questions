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
        crab_num = obj.items.count("crab")
        try:
            # crab_num divis by 4 without remiander
            y = crab_num // 4
            obj.discount = 1.02 * y
        except y == 0:
            print("x not divisable by 4")
        obj.total = obj.sub_total - obj.discount
        print(
            f"""(Baskets subtotal = {obj.sub_total}, Baskets discount = {obj.discount},
            Baskets total = {obj.total} )"""
        )
