class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplier factor

    def __call__(self, value):
        return value * self.factor  # Multiply input by the factor


# ✅ Example Usage
double = Multiplier(2)       # Create a multiplier of 2
triple = Multiplier(3)       # Create a multiplier of 3

# Test with callable()
print(callable(double))      # True — because __call__ is defined

# Call the object like a function
print(double(7))             # 7 * 2 = 1140
print(triple(8))             # 8 * 3 = 24
