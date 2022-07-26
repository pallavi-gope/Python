#write a program to input name, marks and phone number of a student and format it using format function like below:
# The name of the student is abc and his marks are 72 and phone number is 99988899988.

name = input("Enter student name : ")
marks = input("Enter student marks : ")
phone = input("Enter student phone no. : ")

msg = "The name of the student is {0} and his marks are {1} and phone number is {2}".format(name, marks, phone)
print(msg)