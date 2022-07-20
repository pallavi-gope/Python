#Repeat program 4 for a list of such words to be censored.
words = ["donkey", "monkey", "ass", "badword"]
with open('D:\\Python\\Python_Programs\\06_File\\sample.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")

with open('D:\\Python\\Python_Programs\\06_File\\sample.txt', 'w') as f:
    content = f.write(content)