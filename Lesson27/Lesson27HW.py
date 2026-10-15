#You will create a simple account object that stores an account holder name and a private PIN. 
# The program will show that the PIN is safely stored inside the class, try to change the PIN directly from outside, check whether the original private PIN changed, 
# update the PIN correctly using a setter method, and print the account object using __str__().

class Account:
    def __init__ (self, name, pin):
        self.n = name
        self.__p = pin

    def display(self):
        print(f"Account name: {self.n} \nPIN: {self.__p}")

    def update(self, new):
        if len(self.__p) == 4:
            self.__p = new
            print("PIN updated successfully")
        else:
            print("Try again")
        
    def __str__ (self):
        return "Account name" + self.n

account = Account("Allen", "9827")
account.display()
account.__p = 8374
print("Tried to change from outside")
account.update(8374)
account.display()                
