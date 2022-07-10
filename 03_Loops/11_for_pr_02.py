#write a program to greet all the person names stored in a list l1 and starts with S.

l1 = ["Harry", "Larry", "Sarry", "Sara", "Lara"]

for name in l1:
    if name.startswith("S"):
        print("Hello, ", name)
