# Write your solution here
limit = int(input("Limit: "))

count = 1
sum = 0

while sum < limit:
    sum += count
    count+=1
print(sum)