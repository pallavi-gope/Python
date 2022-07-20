#List methods
l1 = [4, 9, 3, 0, 7, 9, 2, 8, 1]
print("List : ", l1)

#1. sort() : Sort the list into ascending order
l1.sort()
print("Sorted List : ", l1)

#2. reverse() : Reverse the list
l1.reverse()
print("Reversed List : ", l1)

#3. append() : Inserts an element at the end of the list
l1.append(10)
print(l1)

#4. insert(index, element) : Inserts an element at a particular index
l1.insert(4, 100)
print(l1)

#5. pop(index) : Deletes the element from the particular index given
l1.pop(1)
print(l1)

#6. remove(element) : Deletes the given element
l1.remove(100)
print(l1)