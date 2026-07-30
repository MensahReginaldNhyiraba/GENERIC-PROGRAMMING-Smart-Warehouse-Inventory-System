from typing import TypeVar, Generic

# Generic type
T = TypeVar('T')

class Inventory(Generic[T]):
    def __init__(self):
        self.items = []

    def store(self, item: T):
        self.items.append(item)

    def retrieve(self):
        return self.items

    def display(self):
        print("Type:", type(self.items[0]).__name__)
        print("Items:", self.items)
        print()


# Product names (string)
products = Inventory[str]()
products.store("Laptop")
products.store("Phone")
products.display()

# Stock quantities (integer)
quantities = Inventory[int]()
quantities.store(50)
quantities.store(120)
quantities.display()

# Product prices (float)
prices = Inventory[float]()
prices.store(4500.99)
prices.store(799.50)
prices.display()

# Batch serial numbers (list)
serial_numbers = Inventory[list]()
serial_numbers.store(["SN001", "SN002", "SN003"])
serial_numbers.store(["SN004", "SN005"])
serial_numbers.display()