# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of Person
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
tchr = Teacher("Mr. Qasim", "AI Agentic") # create class object
tchr.display_info()
