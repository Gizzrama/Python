class Parrot:
    species = "Bird"
    def __init__ (self, name, age):
        self.n = name
        self.a = age

    def display(self):
        print(f"The name is {self.n} and the age is {self.a}.")

a = Parrot("a", 12)
b = Parrot("b", 14)
a.display()
b.display()
