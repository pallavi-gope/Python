#create a class with a class attribute a; create an object with it and set directly a = 0. Does this change the class attribute ?

class Sample:
    a = "Sample"

obj = Sample()
obj.a = 0 #this will create an instance attribute
print(Sample.a)
print(obj.a)

Sample.a = 0 #This will change the class attribute
print(Sample.a)

#instance attribute will create, class attribute will not change.