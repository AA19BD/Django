class Item:
    pay_rate=0.8#class attributes(global attributes)
    def __init__(self, name: str, price: float, quantity=0):#magic methods(__###__)
        # Run validations to receive arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # assigning attributes in __init__(Динамический метод) to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price*=self.pay_rate
   

item1 = Item("Phone", 100, 1)  # instance of the class(object)
# item1.name="Phone" ->assigning attributes to the instance(Топорный метод)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)


print(item1.calculate_total_price())
print(item2.calculate_total_price())

# print(Item.__dict__)#all attributes for Class level
# print(item1.__dict__)#all attributes for Instance level

