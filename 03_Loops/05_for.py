#for loop : for loop is used to iterate through a sequece like list, tuple or string.
fruits = ["Apple", "Banana", "Orange", "Guava", "Grapes", "Mango", "Kiwi"]

for item in fruits:
    print(item)

print("----------------------------------------------")

#Range function in for loop : 
#The range function in python is used to generate  a sequence of numbers, we can also specify the start, end and step-size.
#syntax : range(start, stop, step-size) ; step size is by default 1

for i in range(8): #starts from 0
    print(i)

print("----------------------------------------------")

for i in range(1, 8): #starts from 1
    print(i)
    
print("----------------------------------------------")

for i in range(1, 8, 2): #start 1, stop 8, and step size 2 
    print(i)
