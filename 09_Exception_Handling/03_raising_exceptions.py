#Raising Exceptions : Custom errors can be raise using 'raise' keyword in python.

def increment(num):
    try:
       return int(num) + 1
    except:
        raise ValueError("This is not good!")

a = increment("fasd")
print(a)