# A list contains the multiplication table of 7. write a program to convert it to a verticle string of the same numbers.
l = [str(i*7) for i in range(1,11)]
print(l)
vertical_table = "\n".join(l)
print(vertical_table)