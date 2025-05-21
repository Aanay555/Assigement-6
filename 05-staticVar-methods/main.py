class MathUtils:
    @staticmethod  # statitc method
    def add(a,b):
        return a + b
    
if __name__ == "__main__":
    result = MathUtils.add(10,3)
    print("Total of a and b is = ", result)
