from abc import ABC , abstractmethod

class Shape(ABC):  # abstract class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    
    rect = Rectangle(12,5) # type: ignore
    print("Area of a Rectanlge:", rect.area())




