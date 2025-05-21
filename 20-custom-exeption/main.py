# Step 1: Create a custom exception class
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

# Step 2: Define a function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 to access this resource.")
    else:
        print("Access granted")

# Step 3: Use try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Access denied:", e)
except ValueError:
    print("Please enter a valid number.")
