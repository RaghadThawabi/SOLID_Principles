from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def eat(self):
      pass



class Flyer(ABC):
   @abstractmethod
   def fly(self):
      pass



class Sparrow(Bird, Flyer):
    def __init__(self, name):
        super().__init__(name)


    def eat(self):
        print(self.name + " : Eats")

    def fly(self):
        print(self.name + " : Fly")

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print(self.name + " : Eats")


def main():
    sparrow = Sparrow("Sparrow")
    sparrow.eat()
    sparrow.fly()
    penguin = Penguin("Penguin")
    penguin.eat()

if __name__ == "__main__":
    main()