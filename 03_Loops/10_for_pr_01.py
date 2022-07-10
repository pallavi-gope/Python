#write a program to print the mulitplication table of a given number using for loop.
num = int(input("Enter the Number : "))
for i in range(1, 11):
    # tbl = num * i
    # print(str(num) + " X " + str(i) + " = " + str(tbl)) 
    #F string : used to format string and write variables inside a string
    print(f"{num} X {i} = {num * i}" )

print("------------------------------------------")

j = 1
while j <= 10:
    print(f"{num} X {j} = {num * j}")
    j = j + 1