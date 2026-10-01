#You will create a parent class called Vehicle with shared vehicle details such as brand and maximum speed. 
#Then, you will create a child class called Car that inherits those details, adds its own model and seat information, overrides a method, 
#adds a new method, and confirms the inheritance using issubclass().

class Vehicle:
    def __init__ (self, brand, maximum_speed):
        self.b = brand
        self.ms = maximum_speed
    

class Car(Vehicle):
    def __init__ (self, brand, maximum_speed, model, variant, seat):
        self.m = model
        self.s = seat
        self.v = variant
        super().__init__(brand, maximum_speed)

    def display(self):
        print(f"The {self.b} {self.m} {self.v} has a top speed of about {self.ms}km/h. It can hold up to {self.s} people.")

plaid = Car("Tesla", 322, "Plaid", "Model X SUV", 6)
gemera = Car("Koenigsegg", 400, "Gemera", "HV8", 4)
plaid.display()
gemera.display()

print("Is Car a subcalss of Vehicle?", issubclass(Car, Vehicle))



