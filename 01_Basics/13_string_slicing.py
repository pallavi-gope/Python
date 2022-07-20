# STRING SLICING - A string in python can be sliced for getting a part of a string. 
# The index in a string starts from 0 to (length-1). syntax : sl = name[str_start : str_end] 

msg = "Good Morning, "
name = "Hello" 
print(type(msg)) #get the type of the variable
print(msg + name) #concatenation operation using +
#sting index access
print("Index 0 : ", name[0]) 
print("Index 1 : ", name[1]) 
print("Index 2 : ", name[2]) 
print("Index 3 : ", name[3]) 

#string slicing
print("Index 1 to 4 : ", name[1:4]) #get the 0, 1 and 2 character (excluding 3)
print("Index start to 4 : ", name[:4]) 
print("Index 0 to end : ", name[0:]) 

#negative index in string slicing : opposite counting (when we don't know the length of the string and want to find the last character)
print("Index -1 : ", name[-1])

#slicing with skip values

print("Skip every 2nd character 0 to 5 : ",name[0:4:2])
print("Skip every 2nd character 0 to end : ",name[0::2])
