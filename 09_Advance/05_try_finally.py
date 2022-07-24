## try with finally : python offers a finally clause which means a piece of code irrespective of a exception.
#finally will run even in the case of exception and even after exiting the program. 
#it's generaly use to close files.

try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("Finally we are done")
