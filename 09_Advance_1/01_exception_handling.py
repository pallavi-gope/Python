##Exception Handling: There are many built-in exceptions which are raised in python when something goes wrong.
#Exceptions in python can be handled using a try statement. The code block that handles the exception is called except clause.
#When the exception is handled, the code flow continues without program interruption.
# 

while(True):
    print("Print q to quit")
    a = input("Enter a number : ")
    if a == 'q':
        break
    try:
        a = int(a)
        if(a>6):
            print("You entered the number greater than 6!")
    except Exception as e:
        print(f"Something went wrong : {e}")

print("Thanks for playing this game!")