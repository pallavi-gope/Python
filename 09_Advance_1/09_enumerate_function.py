#Enumerate Function : The Enumerate function adds counter to an iterable and returns it.

l1 = [53, True, 54.5, "Abc"]
for index, item in enumerate(l1):
    print(index, item)

print("*****************************************************************************")
#List Comprehensions : List comprehension is an elegant way to create list based on existing list.

a = [3, 6, 7, 9, 2, 2, 10, 24, 25, 23]
b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)

b = [i for i in a if i%2 == 0] #List comprehension
print(b)

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}  #Set
print(s)
