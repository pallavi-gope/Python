#write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'.

f = open('D:\\Python\\Python_Programs\\06_File\\poem.txt') #open a file
t = f.read() #read the file
if 'Twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close() #close the file