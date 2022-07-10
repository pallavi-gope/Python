#write a program to find the sum of first n natural numbers using while loop.
#NATURAL NUMBER : natural numbers starts from 1. (eg : 1, 2, 3, 4, 5)

n = int(input("Enter the number : "))

i = 1
sum = 0
while(i <= n):
    sum = sum + i
    print(i)
    i = i + 1

print(f"The Sum of First {n} Natural Numbers is : {sum}")