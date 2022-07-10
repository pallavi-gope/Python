#write a program to remove a given word from a string and strip it at the same time.
# STRIPE : Removes the extra spaces

def removeStripeWord(text, word):
    newStr = text.replace(word, "")
    return newStr.strip()

txt = "Hello, This is a brand new programming language called python"
new_txt = removeStripeWord(txt, "brand")
print(new_txt)