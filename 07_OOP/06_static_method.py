#Static Method: Sometimes we need a function that does not use the self parameter, here we can use the static method.

class Employee:
    @staticmethod #decorator
    def greet():
        print("Good Morning Sir")

emp = Employee()
emp.greet()