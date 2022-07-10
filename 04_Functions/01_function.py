# Function : A  function is a group of statements performing a specific task. used to reuse a piece of code.
# When a program gets bigger in size and it's complexity grows, it gets difficult for a programmer to keep track on which piece of code is doing what. 
# A function can be called any number of times and anywhere in the program.
# syntax : 
''' def func1(paramenters):
        statements

Call th: function:
func1(paramenters)
'''
#define function 
def greeting():
    print("Have a Good Day")

greeting()
print("------------------------------------------------------------")

## Types of function
#1. Built-in function : Already built in python; eg. range(), print(), len(), sum() etc. 
#2. User defined function : Defined by user; eg. above we created a function greeting() and percent()

## Function with arguments : A function can accept some values, it can work with. We can put these values in the paranthesis. eg. above percent(marks) function; here marks is the argument, there can be multiple arguments too.
#  Default Parament Function : We can have a function with default argument in the function. that will call if user doest not pass any argument. 
'''
    def func(100)
        pass

    def func(name="Arif")
        print(name)
'''   
marks1 = [45, 50, 60, 70, 80]
marks2 = [48, 63, 87, 55, 84]

# function with arguments
def percent(marks):
    p = sum(marks)/5
    return p

percentage1 = percent(marks1) # call function
percentage2 = percent(marks2)
print(f"Percentage 1 : {percentage1}\nPercentage 2 : {percentage2}")

print("------------------------------------------------------------")

#function with default argument
def greet(name="Stranger"): 
    print("Good Morning, ", name)

greet("Arif")
greet()
