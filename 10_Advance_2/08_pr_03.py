#write a program to filter a list of numbers which are divisible by 5.
l = [5, 10, 13, 90, 28, 88, 85, 40, 43, 26, 20, 55, 59, 50]

a = list(filter(lambda a : a%5 == 0, l))
print(a)
