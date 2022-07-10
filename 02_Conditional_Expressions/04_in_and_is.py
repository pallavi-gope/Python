# 'is' keyword checks the objects and == keyword checks the values
a = None
if(a is None):
    print("Yes")
else:
    print("No")

print("----------------------------------------")
# 'in' keyword checks whether an elment is available in the list or not.
b = [45, 50, 56]
if(45 in b):
    print("Yes")
else:
    print("No")

#Note :- 

#1. There can be any number of elif statements. 
#2. Last else is executed only if all the conditions inside elif if false. else is optional.