# filter() : filter returns the list of items for which the function returns true.
'''     SYNTAX :    list(filter(function, list_name))    '''

def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False 

g10 = lambda num : num > 10

l1 = [1, 2, 4, 3, 5, 6, 8, 90, 20, 0, 30, 4, 50]
print(list(filter(greater_than_5, l1)))
print(list(filter(g10, l1)))