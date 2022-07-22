#1. Single Inheritance : single inheritance occur when a child class inherits a single parent class.
class Employee: #Parent class or base class
    company = "Google"

    def showDetails(self):
        print("This is a employee")

class Programmer(Employee): #child class or derived class
    language = "Python"
    # company = "Youtube"

    def getLang(self):
        print(f"Language is {self.language}")

    def showDetails(self):
        print("This is a programmer")


e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
print(p.company)