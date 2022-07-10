#write a program to find or whether a given name is present in the list or not.
namelist = ["Arif", "Pallavi", "Manini", "Afreen", "Abc", "Xyz"]
yourname = input("Enter Your Name : ")
if(yourname in namelist):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")
