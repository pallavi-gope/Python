#3. Multilevel Inheritance : When a child class becomes a parent from another child class, then it is called multilevel inheritance.

class Person:
    country = "India"
    city = "Jamshedpur"

    def takeBreath(self):
        print("I am Breathing...")

class Company(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")

class Programmer(Company):
    company = "Fiverr"

    def getSalary(self):
        print("No Salary for programmers !")

    def takeBreath(self):
        print("I am an Programmer so I am breathing++...")

p = Person()
c = Company()
pr = Programmer()

p.takeBreath()
c.takeBreath()
pr.takeBreath()

print(pr.country)