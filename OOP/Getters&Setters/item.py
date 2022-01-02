import csv


class Item:
    pay_rate = 0.8  # class attributes(global attributes)
    all = []

    def __init__(self, name: str, price: float, quantity=0):  # magic methods(__###__)
        # Run validations to receive arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # assigning attributes in __init__(Динамический метод) to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator=Read-Only Atrribute
    def name(self):  # getter
        return self.__name

    @name.setter
    def name(self, value):
        if(len(value) > 10):
            raise Exception("This is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod  # decorator
    def instantiate_from_csv(cls):  # class method
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),

            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are points zero(5.0,10.0)
        if isinstance(num, float):  # checking if the receive parameter is instance of float number
            # Count out the floats that are decimal
            return num.is_integer()  # will return True or False
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):  # representation of the object(Имеет доступ к class attributes)
        return f"{self.__class__.__name__}('{self.name}', {self.price},{self.quantity})"
