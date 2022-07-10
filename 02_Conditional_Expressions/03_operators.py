#Relational Operators : Relational operators are used to evaluate conditions inside the if statements.
# == ,<=, >=, >, <, !=

#Logical Operators : In python logical opecators operate on conditional statements.
#1. and : returns true if both conditions are true else returns false
#2. or : return true if any of the condition is true
#3. not : returns oppsite values if true returns false, if false returns true

age = int(input("Enter Your Age : "))
if(age > 34 and age < 50):
    print("You can work with us")
else:
    print("You can't work with us!")

print("----------------------------------------")

if(age > 34 or age < 50):
     print("You can work with us")
else:
    print("You can't work with us!")

print("----------------------------------------")

if(not age > 30):
    print("You are above 20")
else:
    print("You are below 20")

print("----------------------------------------")