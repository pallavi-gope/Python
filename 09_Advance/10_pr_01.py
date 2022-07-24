#write a program to open 3 files 1.txt, 2.txt, 3.txt. if any of these files are not existing, show a message without exiting the program, must be printed prompting the same.
# 
import os
def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile('files/1.txt')
readFile('files/2.txt')
readFile('files/3.txt')