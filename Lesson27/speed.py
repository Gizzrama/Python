class Car:

    def __init__ (self, speed):
        self.__s = speed

    def display(self):
        print("The car speed is", self.__s)

    def updateSpeed(self, new_speed):
        self.__s = new_speed


car1 = Car(40)
car1.display()
car1.updateSpeed(50)
car1.display()

