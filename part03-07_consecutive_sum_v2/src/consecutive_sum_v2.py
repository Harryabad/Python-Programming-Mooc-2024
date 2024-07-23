# Write your solution here
limit = int(input("Limit: "))

count = 1
sum = 0
con_sum = ''

while sum < limit:
    sum += count
    con_sum += str(count) + ' + '
    count+=1
print(f'The consecutive sum: {con_sum[:-3]} = {sum}')