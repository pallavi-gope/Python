#write a program to print the following pattern for n = 3:
'''         
            *
        *   *   *
    *   *   *   *   *
'''
n = 4
for i in range(3):
    # for j in range(n-i-1):
    print(" " * (n-i-1), end="") #to remove the spaces after the print statement
    print("*" * (2*i+1), end="") #to remove the spaces after the print statement
    print(" " * (n-i-1))