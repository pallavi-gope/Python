#Add a static method in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self, num):
        self.number = num
    
    @staticmethod
    def greet():
        print("*****Hello! Welcome to the best calculator!*****")

    def square(self):
        return self.number **2

    def squareRoot(self):
        return self.number **0.5

    def cube(self):
        return self.number **3



n = int(input("Enter a Number : "))
num = Calculator(n)
num.greet()

print("Square is : ", num.square())
print("Square Root is : ", num.squareRoot())
print("Cube is : ", num.cube())