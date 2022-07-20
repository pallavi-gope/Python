## OBJECT ORIENTED PROGRAMMING (OOP)
#-----------------------------------------#

#Solving a problem by creating objects is one of the most popular approaches in programming. This is called Object Oriented Programming.

#This concept focuses using reusable code. (implements DRY [Do Not Repeat Yourself] principle)

## CLASS: A class is a blueprint for creating objects.
# class name should be in pascal case

#class Attribute : An attribute that belongs to the class directly rather than the particular object. eg: Employee class "company" attribute

#Instance Attribute : An Attribute that belongs to the instance (object). eg: Employee class "phone", "salary", "name" attribute

# Pascal case : EmployeeName, SumOfNumber etc.
# Camel case : isNumberic, isFloat etc.

## OBJECT : An object is an instantiation (creating) of a class, when class is defined, a template(info) is defined.
# memory is allocated only after object instantiation. class does not take any memory itself.

# Objects of a given class can invoke the methods available to it without revealing the implementation details to the user.

#self paramenter : self refers to the instance of the class. It is automatically passed with a function call from an object.

##1. ABSTRACTION : A process of handling complexity by hiding unnecessary information from the user. 

##2. ENCAPSULATION : It describes the idea of wrapping data and the methods within one unit. eg: class.


class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print("The sum of a and b is : ",s)

