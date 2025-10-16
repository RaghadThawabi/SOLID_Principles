from abc import ABC, abstractmethod
# add the abstract method for this class
class Discount(ABC):

    @abstractmethod
    def get_the_discount(self):
        pass

#implement the Discount class
class StudentDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def get_the_discount(self):
        print(f"Student discount {self.amount} $")


class TeacherDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def get_the_discount(self):
        print(f"Teacher discount {self.amount} $ ")

def main():
 student_discount = StudentDiscount(100)
 teacher_discount = TeacherDiscount(200)
 student_discount.get_the_discount()
 teacher_discount.get_the_discount()
if __name__ == "__main__":
    main()