from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
        print("Robot works")

class Human(Workable, Eatable):
    def work(self):
        print("Human works")
    def eat(self):
        print("Human eats")

def main():
    robot = Robot()
    robot.work()
    human = Human()
    human.work()
    human.eat()
if __name__ == "__main__":
    main()

