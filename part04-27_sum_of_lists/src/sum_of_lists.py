# Write your solution here

def list_sum(list_a, list_b):
    new_list = []
    for i in range(len(list_a)):
        new_list.append(list_a[i] + list_b[i])
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]