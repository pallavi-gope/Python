#write a program to find out whether a given post is about given word or not.

post = "The weather is really good today, nature is beautiful outside, go and enjoy your day"
word = input("Enter your word : ")

if((word in post) or (word.lower() in post) or (word.upper() in post)):
    print("Present")
else:
    print("Not Present")
