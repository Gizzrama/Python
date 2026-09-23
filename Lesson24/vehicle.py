class Vehicle:
    def __init__ (self, max_speed, mileage):
        self.m = max_speed
        self.mi = mileage


modelY = Vehicle(240, 20)
print("The maximum speed is", modelY.m, "and the mileage is", modelY.mi)

a = int(input("Enter the top speed for modelZ:"))
b = int(input("Enter the mileage to the nearest whole number:"))
modelZ = Vehicle(a, b)
print("The maximum speed is", modelZ.m, "and the mileage is", modelZ.mi)
