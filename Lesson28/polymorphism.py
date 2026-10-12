from abc import ABC, abstractmethod

class ABSClass(ABC):
    def move(self):
        pass

class Human(ABSClass):
    def move(self):
        print("I can walk.")

class Snake(ABSClass):
    def move(self):
        print("I can slither.")

class Dog(ABSClass):
    def move(self):
        print("I can bark.")

class Lion(ABSClass):
    def move(self):
        print("I can roar")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()