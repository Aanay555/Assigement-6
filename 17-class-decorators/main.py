# Step 1: Define the class decorator
def add_greeting(cls):
    # Add a greet() method dynamically
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Attach greet method to the class
    return cls         # Return the modified class

# Step 2: Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Step 3: Use the decorated class
p = Person("Alice")
print(p.greet())  # Output: Hello from Decorator!

