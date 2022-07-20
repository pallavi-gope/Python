#write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up.
d1 = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item",
}
print("Options are : ", d1.keys())
a = input("Enter the Hindi Word : ")
print("The meaning of your word is : ", d1[a]) #it's case sensitive
