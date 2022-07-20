#self paramenter : self refers to the instance of the class. It is automatically passed with a function call from an object.

class Employee:
    company = "Google"
    def getSalary(self): #gives error is remove self
        print(f"Salary for this employee working in {self.company} is {self.salary}")

emp = Employee()
emp.salary = 100000
emp.getSalary() 
# Employee.getSalary(emp) #gives same output
