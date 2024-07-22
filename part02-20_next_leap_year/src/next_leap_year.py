# Write your solution here

year = int(input("Year: "))
nextYr = year + 1

while True:
    if nextYr % 4 == 0 and (nextYr % 100 != 0 or nextYr % 400 == 0):
        print(f"The next leap year after {year} is {nextYr}")
        break
    else:
        nextYr += 1