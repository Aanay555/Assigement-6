
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # Getter method using @property
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter method to update price
    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Deleter method to delete price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# ✅ Example Usage
product = Product(100)

print(product.price)    # Getting price... ➝ 100

product.price = 150     # Setting price...
print(product.price)    # Getting price... ➝ 150

del product.price       # Deleting price...

# print(product.price)  # Will raise AttributeError if uncommented
