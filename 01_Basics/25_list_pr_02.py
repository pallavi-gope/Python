# write a program to accept the marks of 6 students and display then in a sorted manner.

m1 = int(input("Enter Marks of Student 1 : "))
m2 = int(input("Enter Marks of Student 2 : "))
m3 = int(input("Enter Marks of Student 3 : "))
m4 = int(input("Enter Marks of Student 4 : "))
m5 = int(input("Enter Marks of Student 5 : "))
m6 = int(input("Enter Marks of Student 6 : "))

marks = [m1, m2, m3, m4, m5, m6]
marks.sort()
print("Marks : ", marks)