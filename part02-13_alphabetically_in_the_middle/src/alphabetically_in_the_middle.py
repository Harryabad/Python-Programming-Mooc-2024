# Write your solution here
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if (first > second and second > third) or (first < second and second < third):
    print(f"The letter in the middle is {second}")
elif (second > first and first > third) or (second < first and first < third):
    print(f"The letter in the middle is {first}")
elif (second > third and third > first) or (second < third and third < first):
    print(f"The letter in the middle is {third}")
