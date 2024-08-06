# Write your solution here

my_list = []
i = 1
while True:
    print(f"The list is now {my_list}")

    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == 'x':
        print("Bye!")
        break
    elif action == 'd':
        my_list.append(i)
        i += 1
    elif action == 'r':
        i -= 1
        my_list.remove(i)
