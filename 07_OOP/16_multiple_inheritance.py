#2. Multiple Inheritance : Multiple inheritance occurs when a child class inherits from more than one parent class.
class Employee:
    company = "Google"
    empCode = 1234

class Freelancer:
    company = "Fiverr"
    level = 1

    def upgradeLevel(self):
       self.level = self.level + 1
       return self.level

class Programmer(Employee, Freelancer): #properties will priorities according to the class passing here
    name = "Larry"

p = Programmer()
print(p.level)
print(p.upgradeLevel())
print(p.company)