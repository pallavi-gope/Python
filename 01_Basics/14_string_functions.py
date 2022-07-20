import string

story = "hello world, there are some python programs to clear the basics. welcome to python."

# 1. len() : get the length of a string
print("The length of string is : ",len(story)) 

# 2. endswith() : checks whether the string ends with the particular string
print("Story ends with basics : ", story.endswith("basics"))

# 3. count() : count the particular character/string in a string
print("Count of character : ", story.count('a'))

# 4. capitalize() : capitalize the first word of a string
print("Capitalize : ", story.capitalize())

# 5. find() : Finds the position of a particular string/character inside a string
print("Find the string : ", story.find("py"))

# 6. replace(oldword, newword) : Replace the particular word/character in a string
print("Replace : ", story.replace("python", "java"))

