#open and read a file. 
#by default the mode is r
f = open('D:\\Python\\Python_Programs\\06_File\\sample.txt', 'r') #open a file
# data = f.read() #read the file

# data = f.read(15) #can specify the number of characters to read 
# print(data) #print the data

#read first line
data1 = f.readline() #read only the first line from the file.
print(data1)

#read second line
data1 = f.readline() #read only the first line from the file.
print(data1)

f.close() #close the file