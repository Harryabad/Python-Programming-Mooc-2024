# Write your solution here
num = int(input("Please type in a number: "))

i = 1
j = 2

while i <= num:

    if i == num:
        print(i)
        break
    print(j)
    print(i)
    j += 2
    i += 2
