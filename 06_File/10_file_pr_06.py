#write a program to mime a log file and find out whether it contains 'python'.
content = True
i = 0
with open('D:\\Python\\Python_Programs\\06_File\\log.txt') as f:    
    while content:
        i += 1
        content = f.readline()
       
        if 'python' in content.lower():
            print(f"Yes, Python is present at line {i}\n")
            print(content)
        # else:
        #     print("No, Python is not present")

