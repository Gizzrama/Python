#ACP- In this assignment, you will build a Smart Device Command Center using Python. 
#You will use abstraction to create a common smart device structure, create an abstract class with an abstract method, 
#override methods in different device classes, and use polymorphism with shared method names.

from abc import ABC, abstractmethod

class ABSClass(ABC):
    def remote(self):
        print("I am used to control objects.")

class TV(ABSClass):
    def on(self):
        print("The remote is used to turn on the television.")

    def off(self):
        print("The remote is used to turn off the television.")

class Fan(ABSClass):
    def on(self):
        print("The remote is used to turn on the fan.")
    
    def off(self):
        print("The remote is used to turn off the fan.")

class Speaker(ABSClass):
    def on(self):
        print("The remote is used to turn on the television.")
    
    def off(self):
        print("The remote is used to turn off the television.")

tv = TV()
fan = Fan()
s = Speaker()

for self in (tv, fan, s):
    self.on
    self.off
    
    