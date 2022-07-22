##4. INHERITANCE : Inheritance is a way to creating a new class with the existing class.
# we can over write the same functions and methods in derived class

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

'''============================================================================='''

##TYPES OF INHERITANCE IN PYTHON

#1. Single Inheritance
#2. Multiple Inheritance
#3. Multilevel Inheritance