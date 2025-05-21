# Step 1: Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Call the original function
    return wrapper

# Step 2: Apply the decorator to say_hello using @ syntax
@log_function_call
def say_hello():
    print("Hello, world!")

# Step 3: Call the decorated function
say_hello()
