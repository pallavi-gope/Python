# map() : map applies a function to all the items in an input list.
'''
SYNTAX:
    map(function, input_list)
'''

def square(num):
    return num * num

l1 = [1, 2, 4]
l2 = []

#Method 1
# for item in l1:
#     l2.append(square(item))

#Method 2
print(list(map(square, l1)))

# print(l1)
# print(l2)