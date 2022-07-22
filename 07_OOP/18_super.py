## super() method is used to access the methods of super class or parent class inside a derived class.
class Person:
    country = "India"
    city = "Jamshedpur"

    def __init__(self):
        print("\nInitializing Person.....\n")    

    def takeBreath(self):
        print("I am Breathing...")

class Company(Person):
    company = "Honda"

    def __init__(self):
        # super().__init__()
        print("\nInitializing Company.....\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath() #runs the base class takebreath() function too
        print("I am an Employee so I am luckily breathing...")

class Programmer(Company):
    company = "Fiverr"

    def __init__(self):
        print("\nInitializing Programmer.....\n")

    def getSalary(self):
        print("No Salary for programmers !")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am breathing++...")

p = Person()
c = Company()
pr = Programmer()

# p.takeBreath()
# c.takeBreath()
pr.takeBreath()

print(pr.country)