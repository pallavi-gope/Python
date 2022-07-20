class Employee:
    company = "Google" #class attribute
    salary = 100

emp1 = Employee()
emp2 = Employee()

emp1.salary = 50000 #instance attribute
emp2.salary = 40000

print(f"{emp1.company} - {emp1.salary}")
print(f"{emp2.company} - {emp2.salary}")

Employee.company = "Youtube"
print(emp1.company)
