class Countdown:
    def __init__(self, start):
        self.current = start  # starting value

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop iteration when countdown finishes
        value = self.current
        self.current -= 1
        return value

# ✅ Example usage
for number in Countdown(7):
    print(number)

