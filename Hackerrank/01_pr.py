
l = []
second_lowest_names = []
scores = set()
stud = [["Harsh", 20], ["Beria", 20], ["Varun", 19], ["Kakunami", 19], ["Vikas", 21]]
for i in stud:
    l.append(i)
    scores.add(i[1])

second_lowest = sorted(scores)[1]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name)
