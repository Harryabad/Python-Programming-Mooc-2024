# Write your solution here

def length_of_longest(my_list):
    longest_word = 0
    for i in my_list:
        if len(i) > longest_word:
            longest_word = len(i)
    return longest_word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)