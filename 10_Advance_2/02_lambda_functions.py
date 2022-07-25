#Lambda Functions : functions created using an expression using "lambda" keyword. also called anonymous functions and can be used as normal functions.
'''  SYNTAX
        function name = lambda arguments : expression
'''

# def func(a):
#     return a + 5

#lambda functions
func = lambda a : a + 5 
square = lambda x : x * x
sum = lambda a, b, c : a + b + c

x = 500
print(func(x))
print(f"Square : {square(x)}")
print(f"Sum : {sum(x, 4, 4)}")