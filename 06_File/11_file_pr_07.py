#write a program to make the copy of a file 'this.txt'
with open('D:\\Python\\Python_Programs\\06_File\\this.txt') as f:
    content = f.read()

with open('D:\\Python\\Python_Programs\\06_File\\copy.txt', 'w') as f:
    f.write(content)