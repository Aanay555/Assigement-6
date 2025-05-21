class Employee:
    def __init__(self,name):
        self.name = name
class Department:
    def __init__(self, employee):
        self.emplyee = employee

    def show_employee(self):
        print(f"Employee in Department : {self.emplyee.name}")

if __name__ =="__main__":
    emply = Employee("UZMA")
    deprt = Department(emply)  # reference of 1st class (emply)
    deprt.show_employee()