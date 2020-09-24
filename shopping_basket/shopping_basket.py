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
                    if self.sub_total < 0.0:
                        self.sub_total = 0.0
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
            obj.discount += 1.02 * y
        except y == 0:
            print("crab_num not divisable by 4")
        try:
            obj.total = obj.sub_total - obj.discount
        except obj.total < 0.0:
            obj.total = 0.0
        print(
            f"""(Baskets subtotal = {obj.sub_total}, Baskets discount = {obj.discount},
            Baskets total = {round(obj.total, 2)} )"""
        )


class Bonus:
    def __init__(self, obj):
        fish_num = obj.items.count("fish")
        shark_num = obj.items.count("shark")
        try:
            # fish_num divis by 3 without remiander
            y = fish_num // 3
            obj.discount += 2.1 * y
            print(obj.discount)
        except y == 0:
            print("fish_num not divisable by 3")
        try:
            # shark_num divis by 2 without remiander
            y = shark_num // 3
            obj.discount += 5.0 * y
            print(obj.discount)
        except y == 0:
            print("shark_num not divisable by 3")
        try:
            obj.total = obj.sub_total - obj.discount
        except obj.total < 0.0:
            obj.total = 0.0
        print(
            f"""(Baskets subtotal = {round(obj.sub_total, 2)},
            Baskets discount = {round(obj.discount, 2)},
            Baskets total = {round(obj.total, 2)} )"""
        )
