# Write your solution here
age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")
if age >=0 and age < 5:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")