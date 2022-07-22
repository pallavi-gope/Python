#create a class Employee and add salary and increment properties to it.
#write a method salary after increment method with a @property decorator with a setter which changes the value of increment based on salary.

class Employee:
    salary = 50000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(f"Salary befor increment : {e.salaryAfterIncrement}")
print(f"Salary Increment before setter : {e.increment}")
e.salaryAfterIncrement = 80000
print(f"Salary Increment after setter : {e.increment}")
print(f"Salary after setter : {e.salaryAfterIncrement}")
