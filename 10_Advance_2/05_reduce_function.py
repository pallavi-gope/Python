# reduce() : reduce applies a rolling computation to sequential pair of elements.
'''
    SYNTAX:     
       from functools import reduce 
       reduce(function, list)
''' 

from functools import reduce
l1 = [1, 2, 3, 4]

sum = lambda a, b : a + b

val = reduce(sum, l1)       #this will add the values like : 1 + 2 > 3 + 3 > 6 + 4 = 10
print(val)