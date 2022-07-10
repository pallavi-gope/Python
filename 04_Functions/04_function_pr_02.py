#write a program to convert tempearture celsius to farenheit. 
#FORMULA : F = C×(9/5)+32

def temp(cel):
    f = (cel * (9/5)) + 32
    return f

temperature = temp(0)
print("Farenheit Temperature is : ", temperature)

print("------------------------------------------------")

#prevent new line in print function. by default print ends with \n
print("Hello", end=" ")
print("How", end=" ")
print("Are", end=" ")
print("You?", end=" ")