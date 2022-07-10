#write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter 1st Subject Marks : "))
sub2 = int(input("Enter 2nd Subject Marks : "))
sub3 = int(input("Enter 3rd Subject Marks : "))

percentage = (sub1 + sub2 + sub3)/3

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail")
elif(percentage >= 40):
    print("Congratulations! You are pass")
else:
    print("You are fail")




