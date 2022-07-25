#1. join() : Creates a string from iterable objects.

l1 = ["Camera", "Laptop", "Phone", "iPad", "Hard Disk", "Commputer"]

sentence = " ~ ".join(l1)
print(sentence)

#2. format() : Used before f string form formatting the strings.

name = "your name"
rollno = "your roll no."
# a = "This is {} and this is {}".format(name, rollno)
a = "This is {1} and this is {0}".format(name, rollno)
print(a)
