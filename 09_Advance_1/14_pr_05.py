#store the multiplication tables generated in problem 3 in a file named "table.txt"

num = int(input("Enter your number : "))
table = [num*i for i in range(1, 11)]
print(str(table))

with open('files/tables.txt', 'a') as f:   
    f.write(str(table)) 
    f.write('\n')