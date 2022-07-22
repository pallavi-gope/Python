#getter : the name with property decorator is called getter.
#setter : getterPropertyName.setter will create a setter.

class Employee:
    company = "Wipro"
    salary = 50000
    bonus = 5000
    
    @property     #also call getter (property decorator)              
    def totalSalary(self):                  #it's a function but behaves like property
        return self.salary + self.bonus

    @totalSalary.setter     #setter
    def totalSalary(self, val):
        self.bonus = val - self.salary

e = Employee()
print(f"Total Salary : {e.totalSalary}")        #behaves like property
e.totalSalary = 60000
print(f"Salary : {e.salary}")
print(f"Bonus : {e.bonus}")
print(f"Total Salary : {e.totalSalary}") 