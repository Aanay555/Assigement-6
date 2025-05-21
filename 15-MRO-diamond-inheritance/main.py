class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):
    pass

# Create object of D and call show()
obj = D()
obj.show()

# Print MRO for clarity
print(D.__mro__)
