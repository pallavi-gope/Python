#write a program to generate multiplication table from 2 to 20 adn write it to the different files place these files in a folder for a 13 year old.

for i in range(2, 21):
    with open(f"D:\\Python\\Python_Programs\\06_File\\tables\\multiplication_table_{i}", 'w') as f:
        for j in range(1, 11):       
            f.write(f"{i} x {j} = {i*j}")
            if j != 10:
                f.write('\n')
    