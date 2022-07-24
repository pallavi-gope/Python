# global keyword : global keyword is used to modify the variable outside of the current scope.
a = 54   #global variable
def func1():
    global a    #use global variable, a = 18 will change the global variable
    print(f"Print statement 1 : {a}")
    a = 18  #local variable  
    print(f"Print statement 2 : {a}")

func1()
print(f"Print statement 3 : {a}")