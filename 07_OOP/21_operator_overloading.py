# Operator Overloading : Operator overloading in python can be done with dunder methods (special methods like __init__() etc.)
#These methods are called when a given operator is used on the objects.

class Number:
    #in-built dunder functions in python for operator overloading
    def __init__(self, num1):
        self.num = num1

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num3):
        print("Let's Multiply")
        return self.num * num3.num


n1 = Number(4)
n2 = Number(10)
sum = n1 + n2
mul = n1 * n2
print(f"Sum : {sum}")
print(f"Multiplication : {mul}")


#DUNDER METHODS :

#1. ADD             --->           __add__()
#2. SUBSTRACTION    --->           __sub__()
#3. MULTIPLICATION  --->           __mul__()
#4. DIVIDE          --->           __truediv__()
#5. // OVERLOAD     --->           __floordiv__()