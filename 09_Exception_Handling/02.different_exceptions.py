try:
    a = int(input("Enter a number : "))
    c = 1/a
except ValueError as e:
    print("Please enter a valid number!")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")
except Exception as e:
    print("Exception Occured")
    print(e)

print("Thanks for using this code")