#break statement : break used to come out of the loop.
for i in range(1, 10):
    print(i)
    if i == 5:
        break
else:
    print("Done") #executes only on successfully termination of the loop, won't work here as using break statement.
   