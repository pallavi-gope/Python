#write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username : ")
if(len(username) < 10):
    print("Incorrect Username")
else:
    print("Correct Username")
