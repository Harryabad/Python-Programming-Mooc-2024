# Write your solution here
my_list = []

while True:
    new = int(input("New item: "))
    if new == 0:
        print("Bye!")
        break
    else:
        my_list.append(new)
        print(f"The list now: {my_list}")
        print(f"The list in order: {sorted(my_list)}")