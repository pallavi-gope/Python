#write a program to find the grade of a student from his marks with the following scheme.
# [90-100 : Ex], [80-90 : A], [70-80 : B], [60-70 : C], [50-60 : D] [<40 : F]

marks = int(input("Enter Your Marks : "))
if(marks >= 90):
   grade = "Ex"
elif(marks >= 80):
    grade = "A"
elif(marks >=70):
    grade = "B"
elif(marks >= 60):
     grade = "C"
elif(marks >= 50):
    grade = "D"
else:
     grade = "F"

print("Your Grade is " + grade)