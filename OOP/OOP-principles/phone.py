from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):  # magic methods(__###__)
        # Call super().__init__() function to have access to all attributes and methods of parent class
        super().__init__(  # Item class will keep everything that was created in  child class,due to super() method
            name, price, quantity
        )
        # Run validations to receive arguments
        assert broken_phones >= 0, f"Broken_phones {broken_phones} is not greater than or equal to 0"
        # assigning attributes in __init__(Динамический метод) to self object

        self.broken_phones = broken_phones
