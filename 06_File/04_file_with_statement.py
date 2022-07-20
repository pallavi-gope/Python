# with statement : open and close the file automatically.

with open('D:\\Python\\Python_Programs\\06_File\\sample.txt', 'a') as f:
    a = f.write("I am automatic")

with open('D:\\Python\\Python_Programs\\06_File\\sample.txt', 'r') as f:
    a = f.read()

print(a)