class Emplyee:
    def __init__(self, name,  salary, ssn): # constructor with parameters
        self.name = name  # public variable

        self._salary = salary # protected variable/semi private variable

        self.__ssn = ssn  # private variable

if __name__ == "__main__":
    emply = Emplyee("uzma", 60000 ,"1112-889-9998")
    # acces public variable
    print("Public Var:" , emply.name)
    print("Protected Var:" , emply._salary)

    # acces public variable with try/except
    try:
        print("Private Var:" , emply.__ssn)
    except AttributeError:
        print("private variable is not accees outsite from class")



