# write a program to fill in a letter template given below with name and date
# letter = '''Dear <Name>
#             You are selected!
#             <Date>'''

letter = '''Dear <| NAME |>,
Greetings from ABC company. I am happy to tell you about your selection.
You are selected!
Have a great day!

Thanks and Regards!
HR ABC company
Date : <| DATE |> 
'''
name = input("Enter Name : ")
date = input("Date : ")

letter = letter.replace('<| NAME |>', name)
letter = letter.replace('<| DATE |>', date)
print(letter)
