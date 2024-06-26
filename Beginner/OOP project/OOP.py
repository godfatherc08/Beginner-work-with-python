class Item:
    def calculate_total_price(self, x, y):
        return x*y


item1 = Item()
item1.name = "Phone"
item1.quantity = 100
item1.price = 50

print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.quantity = 300
item2.price = 100
