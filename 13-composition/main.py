class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self):
        self.engine = Engine()  #COMPOSITION (it made an object of engine class mean 1st class)

    def start_car(self):
        self.engine.start()  # call method of Engine class

if __name__ == "__main__":
    may_car = Car()
    may_car.start_car()        