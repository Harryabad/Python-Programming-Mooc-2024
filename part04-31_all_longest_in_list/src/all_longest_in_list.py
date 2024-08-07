# Write your solution here

def all_the_longest(my_list):
    word = 0
    longest = []
    for i in my_list:
        if len(i) > word:
            word = len(i)
            longest = [i]
        elif len(i) == word:
            longest.append(i)
    return longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']