##try with else clause : Sometimes we want to run a code when try was successful. else block will execute when try will execute.

try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("Successful")
