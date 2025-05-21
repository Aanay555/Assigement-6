class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self): #   public method
        print(f"{self.brand} is starting .....")

if __name__ == "__main__":
    cultus_car = Car("Suzuki Cultus")  # access public var and method outsite of class
    cultus_car.start()        