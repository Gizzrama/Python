from abc import ABC, abstractmethod

class ABSClass(ABC):
    def print(self, x):
        print("The value of x is", x)

    def task(self):
        print("We are inside ABS class.")


class TestClass(ABSClass):
    def task(self):
        print("We are inside TestClass.")

testObj = TestClass()
testObj.task()
testObj.print(50)


