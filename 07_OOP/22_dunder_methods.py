class DunderMethods:
    def __init__(self, num1):
        self.num = num1

    #shows any string or number
    def __str__(self):
        return f"Decimal Number : {self.num}"

    #to set the length 
    def __len__(self):
        return 1

n = DunderMethods(9)
print(n)
print(len(n))