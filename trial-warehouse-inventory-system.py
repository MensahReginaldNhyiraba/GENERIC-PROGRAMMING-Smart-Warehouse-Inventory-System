from typing import TypeVar, Generic

# Create a generic type
T = TypeVar('T')

# Generic class
class Storage(Generic[T]):
    def __init__(self):
        self.item = None

    def store(self, item: T):
        self.item = item

    def retrieve(self) -> T:
        return self.item


# Integer example
int_storage = Storage[int]()
int_storage.store(100)
print("Integer:", int_storage.retrieve())

# String example
string_storage = Storage[str]()
string_storage.store("Electrical Engineering")
print("String:", string_storage.retrieve())

# List example
list_storage = Storage[list]()
list_storage.store([1, 2, 3, 4, 5])
print("List:", list_storage.retrieve())