#__name__ : evaluates the name of the module in python from where the program is ran.
#If the module is being run directly from the command line, the __name__ is set to string "__main__".
#Thus this behaviour is used to check whether the module is run directly or imported to another file.

def greet(name):
    print(f"Good morning {name}")

#This portion will execute when executing the main file i.e. this file, but will not execute when importing somewhere else.
# print(__name__)
if __name__ == '__main__':
    n = input("Enter a name : ")
    greet(n)