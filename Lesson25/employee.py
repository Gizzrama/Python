class employee:
    def __init__ (self, name, age, service):
        self.n = name
        self.a = age
        self.s = service

    def __del__(self):
        print("Object is deleted")

    def display(self):
        print(f"The name is {self.n}, the age is {self.a} and the service is {self.s}.")

employee1 = employee("Srihari", 20, 1)
employee1.display()

employee2 = employee("Aarav", 25, 5)
employee2.display()

del employee1
employee1.display()