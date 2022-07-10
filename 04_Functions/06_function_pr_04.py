#write a program to print the first n lines of the follow pattern:
'''
        *  *  *  *  *  *  *
        *  *  *  *  *  *
        *  *  *  *  *
        *  *  *  * 
        *  *  * 
        *  * 
        *
'''

def pattern(n):
    for i in range(n):
        print(" * " * (n-i))

num = int(input("Enter the number : "))
pattern(num)