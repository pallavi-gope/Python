#A spam comment is defined as a text containing following keywords:
#"make a lot of money", "buy now", "subscribe this", "click this".
#write a program to detect these.

s1 = input("Enter the text : ")
if("make a lot of money" in s1):
    spam = True
elif("buy now" in s1):
    spam = True
elif("subscribe this" in s1):
    spam = True
elif("click this" in s1):
    spam = True
else:
    spam = False

if(spam):
    print("This text is a spam.")
else:
    print("This text is not spam.")