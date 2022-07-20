#write a program to find out whether a file is identical and matches the content of another file.

file1 = 'D:\\Python\\Python_Programs\\06_File\\this.txt'
file2 = 'D:\\Python\\Python_Programs\\06_File\\copy.txt'

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")