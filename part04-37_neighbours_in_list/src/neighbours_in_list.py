# Write your solution here

def longest_series_of_neighbours(my_list):
    new_list = []
    max_size = 0

    for i in my_list:
        if not new_list or i == new_list[-1] + 1 or i == new_list[-1] - 1:
            new_list.append(i)
        else:
            new_list = [i]  

        if len(new_list) > max_size:
            max_size = len(new_list)

    return max_size


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))