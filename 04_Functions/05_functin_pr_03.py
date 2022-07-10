#write a recursive function to find the sum of n natural numbers.
num = int(input("Enter a number : "))
def sumOfNatural(n):
    if n == 0:
        return 0
    return sumOfNatural(n-1) + n

sum_of_nums = sumOfNatural(num)
print(f"Sum of {num} Natural Numbers is {sum_of_nums}")