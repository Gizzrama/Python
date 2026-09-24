#You will create a simple pet profile system. The program first creates a basic Pet class and one object. 
#Then it creates a PetProfile class with a class attribute and instance attributes. 
#You will create two pet objects and print their details using attributes stored with self.

class pet:
    print("This is a pet.")

class PetProfile:
    category = "pet"
    def __init__ (self, name, animal_type, age, favourite_food):
        self.n = name
        self.at = animal_type
        self.a = age
        self.f = favourite_food

    def display(self):
        print(f"The animal's name is {self.n} and it is a {self.at}. It is {self.a} years old and its favourite food is {self.f}.")

pet_object = pet()

pet1 = PetProfile("Charlie", "dog", 4, "peanut butter")
pet2 = PetProfile("Bella", "cat", 2, "tuna")

pet1.display()
pet2.display()
