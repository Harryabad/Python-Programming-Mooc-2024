# Write your solution here
my_list = []
while True:
    string = input("Exam points and exercises completed: ")
    if string == "":
        break
    x = string.split()
    my_list.append([int(x[0]), int(x[1])])

#print(my_list)
print("Statistics: ")

avg = 0
for i in my_list:
    avg += i[0] + (int(i[1]/10))
avg = avg / len(my_list)

print(f"Points average: {avg:.1f}")

five, four, three, two, one, zero, fail = 0,0,0,0,0,0,0

for i in my_list:
    i[1] = int(i[1]/10)

for i in my_list:
    if i[0] < 10 or ((i[0] + i[1]) >= 0 and (i[0] + i[1]) <= 14):
        fail += 1
        zero += 1
    elif (i[0] + i[1]) >= 15 and (i[0] + i[1]) <= 17:
        one += 1
    elif (i[0] + i[1]) >= 18 and (i[0] + i[1]) <= 20:
        two += 1
    elif (i[0] + i[1]) >= 21 and (i[0] + i[1]) <= 23:
        three += 1
    elif (i[0] + i[1]) >= 24 and (i[0] + i[1]) <= 27:
        four += 1
    elif (i[0] + i[1]) >= 28 and (i[0] + i[1]) <= 30:
        five += 1






print(f"Pass percentage: {100 - (fail/len(my_list))*100:.1f}")
print("Grade distribution: ")
print(f"  5: {'*'*five}")
print(f"  4: {'*'*four}")
print(f"  3: {'*'*three}")
print(f"  2: {'*'*two}")
print(f"  1: {'*'*one}")
print(f"  0: {'*'*zero}")
