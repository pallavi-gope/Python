#class methods : A class method is the method which is bound to the class and not the object of the class.
# "@classmethod" decorator is used to create a class method. this will avoid the self parameter.
# can be used the change the class attribute

class Employee:
    company = "Microsoft"
    salary = 50000
    location = "Hyderabad"

    # def changeSalary(self, salary):
    #     self.__class__.salary = salary

    @classmethod
    def changeSalary(cls, salary): 
        cls.salary = salary         #change the class attribute

e = Employee()
e.changeSalary(70000)
print(e.salary)
print(Employee.salary)
