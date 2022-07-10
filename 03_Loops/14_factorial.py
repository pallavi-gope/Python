#write a program to find the factorial of a given number
#5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number : "))
fact = 1
for i in range(1, num+1):
    fact = fact * i

print(f"Factorial of {num} is : {fact}")