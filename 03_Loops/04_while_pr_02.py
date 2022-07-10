#write a program to print the content of a loop using while loop.
fruits = ["Apple", "Banana", "Orange", "Guava", "Grapes", "Mango", "Kiwi"]
i = 0
while(i < len(fruits)):
    print("Fruit " + str(i) + " : ", fruits[i])
    i = i+1