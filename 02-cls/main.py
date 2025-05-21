class Counter:
    count =0 # object of counter class


    def __init__(self):
        Counter.count +=1

    @classmethod
    def showing_counter(cls):
        print(f"Total objects are created: {cls.count}")
if __name__ == "__main__":
    object1 = Counter()
    object2 = Counter()
    object3 = Counter()
    object4 = Counter()
    Counter.showing_counter()