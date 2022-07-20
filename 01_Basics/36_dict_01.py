#Create an empty dictionary, allow 4 friends to enter their favourite language as values and use the keys as their names. Assume that the name are unique.
favlang = {}
l1 = input("Enter your favourite language friend1 : ")
l2 = input("Enter your favourite language friend2 : ")
l3 = input("Enter your favourite language friend3 : ")
l4 = input("Enter your favourite language friend4 : ")

favlang['friend1'] = l1
favlang['friend2'] = l2
favlang['friend3'] = l3
favlang['friend4'] = l4

print(favlang)

#Q. What will happen if two friends name are same?
#A. Language will update with the latest value.

#Q. What will happen if two language names are same?
#A. values are not necessary to be unique, only keys need to be unique.
