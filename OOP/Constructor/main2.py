class Item:
    pay_rate = 0.8  # class attributes(global attributes)
    all = []

    def __init__(self, name: str, price: float, quantity=0):  # magic methods(__###__)
        # Run validations to receive arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # assigning attributes in __init__(Динамический метод) to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    def __repr__(self):  # representation of the object(Имеет доступ к class attributes)
        return f"Item('{self.name}', {self.price},{self.quantity})"


item1 = Item("Phone", 100, 1)  # instance of the class(object)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all) #[Item('Phone', 100,1), Item('Laptop', 1000,3), Item('Cab....
#Было до __repr__ <__main__.Item object at 0x10e85d2b0>
# for instance in Item.all:
#     print(instance.name) #Phone,Laptop,...
