#write a program to print the multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

num = int(input("Enter a number : "))
table(num)