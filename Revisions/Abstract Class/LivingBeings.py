from abc import ABC, abstractmethod


class LivingBeings(ABC):
    @abstractmethod
    def doAction(self):
        pass


class Human(LivingBeings):
    def doAction(self):
        print("I am speakings...")


class Dog(LivingBeings):
    def doAction(self):
        print("I am barking...")


class Cat(LivingBeings):
    def doAction(self):
        return "I am meowing...."


H = Human()
H.doAction()

D = Dog()
D.doAction()

C = Cat()
print(C.doAction())



##When we create an object for the abstract class it raises an error.
## a = Animal()  # ❌ Error! Can't instantiate abstract class