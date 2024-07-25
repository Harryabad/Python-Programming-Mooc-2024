# Write your solution here

num = int(input("Please type in a number: "))
i = 1
count = 1
while i <=  num:
    
    print(f"{i} x {count} = {i * count}")

    count += 1

    if count > num:
        i += 1
        count = 1
