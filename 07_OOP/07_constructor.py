##3. CONSTRUCTOR

# __init__() : this is a special method (functin) that is first runs as soon as the object is created. No need to call explicitly

#__init__() method is also known as constructor. It takes self argument and can also take further arguments.

class Employee:
    company = "Google"
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        print("Employee is created!")
    def getDetails(self):
        print(f"The Name of the Employee : {self.name}")
        print(f"The Salary of the Employee : {self.salary}")
        print(f"The Designation of the Employee : {self.designation}")

emp = Employee("Arif", 100000, "Software Engineer")
emp.getDetails()
