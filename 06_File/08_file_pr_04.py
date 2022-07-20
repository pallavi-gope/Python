#A file contains a word "Donkey" multiple times. you need to write a program which replaces the word with ###### by updating the same file.

with open('D:\\Python\\Python_Programs\\06_File\\sample.txt') as f:
    content = f.read()

content = content.replace("donkey", "######")

with open('D:\\Python\\Python_Programs\\06_File\\sample.txt', 'w') as f:
    content = f.write(content)