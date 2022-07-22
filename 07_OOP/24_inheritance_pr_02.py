#create a class Pets from a class Animals and further create class Dog from Pets. add a method bark to class Dog.

class Animals:
    animal = "Cat"

class Pets(Animals):
    color = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog is barking")

d = Dog()
d.bark()