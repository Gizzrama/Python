class FamilyMember:
    def intro(self):
        print("This is a parent class intro function.")

    def __init__ (self, height, eye_colour):
        self.h = height
        self.ec = eye_colour

    def display1(self):
        print("This is a parent class.")
        print(f"The height is {self.h} and the eye colour is {self.ec}.")

class Child(FamilyMember):
        
    def __init__ (self, name, age, height, eye_colour):
        self.n = name
        self.a = age
        super().__init__(height, eye_colour)

    def display(self):
            print(f"The name is {self.n} and the age is {self.a}")
            
a = Child("Jack", 15, 175, "black")
a.intro()
a.display()
a.display1()