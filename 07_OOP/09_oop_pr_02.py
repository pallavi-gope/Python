#write a class Calculator capable of finding square cube and square root of a number.
class Calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        return self.number **2

    def squareRoot(self):
        return self.number **0.5

    def cube(self):
        return self.number **3

n = int(input("Enter a Number : "))
num = Calculator(n)

print("Square is : ", num.square())
print("Square Root is : ", num.squareRoot())
print("Cube is : ", num.cube())