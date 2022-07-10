#write a program to convert inches into centimeters.
#FORMULA : 1 in = 2.54 cm

def inchToCm(inch):
    return inch * 2.54

num = float(input("Enter inch : "))
print("Cm is : ", inchToCm(num))