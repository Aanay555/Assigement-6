class Bank:
    bank_name = "Meezan Bank"  # class variable

    @classmethod
    def change_bank_name(cls, name):  # class method
        cls.bank_name = name


if __name__ == "__main__":
    usr1 = Bank()
    usr2 = Bank()

    print("Real bank name:")  # real bank name
    print(f"usr1 bank name:{usr1.bank_name}")
    print(f"usr2 bank name:{usr2.bank_name}") 

    Bank.change_bank_name("Allied Bank")        

    print("\nAfter changing Bank's Name: ")
    print(f"usr1 bank name:{usr1.bank_name}")
    print(f"usr2 bank name:{usr2.bank_name}") 
    