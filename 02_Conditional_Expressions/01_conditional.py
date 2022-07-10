#Conditional Expressions: In pytho, we are able to execute instructions on a condiotion(s).

##1. IF ELSE AND ELIF STATEMENTS:
# if else and elif statements are the multiway decision taken by our program due to certain condition in our code.
#Indentation: Spaces before the next line to if or elif or else.
# syntax : 
# if(condition) : 
#     print("Yes")
# elif(condition):
#     print("No")
# else :
#     print("May be")

a = 45

# if-elif-else ladder
if(a < 30):
    print("a is greater than 30")
elif(a < 50):
    print("a is greater than 50")
else:
    print("a is smaller than all values")

# multiple if statements
if(a > 10):
    print("a is greater than 10")
if(a > 20):
    print("a is greater than 20")
if(a > 30):
    print("a is greater than 30")
else:
    print("a is smaller")
