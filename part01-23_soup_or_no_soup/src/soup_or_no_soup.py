# Write your solution here
name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    portions = int(input("How many portions of soup? "))
    print(f"The total cost is {5.90 * portions}\n Next please!")