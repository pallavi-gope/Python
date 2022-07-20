#File I/O : A File is data stored in a  storage device. A python program can talk to the file by reading content from it and writing content to it.

#Types of file:
#1. Text files (.txt, .c etc.)
#2. Binary files (.jpg, .png, etc.)

#Python has a lots of function to reading, writing, updating and deleting a file
'''-------------------------------------------------------------'''

## OPENING A FILE

#1. open(): Open a file. It takes two parameters filename and mode. eg: open('file.txt', "r") 
#2. read(): Read a file.
#3. readline() : Read one line from the file.

## Modes of opening a file:
#1. r -> open for reading
#2. w -> open for writing
#3. a -> open for appending
#4. + -> open for udpating

# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode (default mode) 

'''-------------------------------------------------------------'''

## WRITING A FILE

# In order to write a file, we first open it in write mode or append mode after which we use,
# Python's f.write() method to write in the file  


