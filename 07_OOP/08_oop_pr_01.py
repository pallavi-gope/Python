#create a class programmer for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"This name of the {self.company} programmer is {self.name} and the name of the product is {self.product}")

emp1 = Programmer("Pallavi", "VS Code")
emp2 = Programmer("Arif", "Windows")

emp1.getInfo()
emp2.getInfo()