#Set methods
a = set()

#1. add() : adds elements
a.add(1)
a.add(2)
a.add(3)
a.add(6)
print(a)
# cannot add list and dictionary inside a set as it's mutable.
# can add tuple inside the set immutable.

#2. len() : returns the lenth of the set
print(len(a))

#3. remove() : removes an element from the set
a.remove(1)
print(a)

#4. pop() : removes an item and returns the deleted item
print(a.pop())
print(a)

#5. clear() : empty the set
a.clear()
print(a)