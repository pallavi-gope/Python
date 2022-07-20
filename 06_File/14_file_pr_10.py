#write a program to rename a file to "renamed_by_python".
import os

oldname = 'D:\\Python\\Python_Programs\\06_File\\newfile2.txt'
newname = "D:\\Python\\Python_Programs\\06_File\\renamed_by_python.txt"
#read old file
with open(oldname) as f:
    content = f.read()

#write in new file
with open(newname, 'w') as f:
    f.write(content)

os.remove(oldname)