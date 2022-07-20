#can you change the self parameter inside a class to something else.
class Sample:
   def __init__(slf, name):
      slf.name = name
        
obj = Sample("My Name")
print(obj.name)

# Yes self parameter can be change. It's like a function parameter.
