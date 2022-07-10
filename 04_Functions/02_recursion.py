#Recursion : Recursion is a function which calls itself inside a function. basically used to utilize the mathematical formulas.

# write a program to find the factorial of a number using function.
# n! = 1 x 2 x 3 ...... x n
# n! = [1 x 2 x 3 x .... x (n-1)] x n
# n! = (n-1) x n
 
def fact(n):
    f = 1
    for i in range(n):
        f = f * (i+1)
    return f

#recursive function
def fact_rec(n):
    if n == 1 or n == 0:
        return 1
    return n * fact_rec(n-1) #function calling itself

print(fact(5))
print(fact_rec(5))

# NOTE : need to be careful when writing recursive function. sometimes it can be infinite.