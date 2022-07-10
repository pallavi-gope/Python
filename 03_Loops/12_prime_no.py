#write a program to check whether a given number is prime or not.
#PRIME NUMBER : divides by 1 or itself.

num = int(input("Enter the Number : "))
prime = True
for i in range(2, num):
    if(num % i == 0):
        prime = False
        break        

if prime: 
    print("\nThis Number is Prime!\n")
else:
    print("\nThis Number is not Prime!\n")
