# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1 or index >= len(my_list):
        break
    value = int(input("New Value: "))
    my_list[index] = value
    print(my_list)