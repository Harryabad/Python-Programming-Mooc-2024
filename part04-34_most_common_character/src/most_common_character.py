# Write your solution here
def most_common_character(string):

    dictionary = {}

    for i in string:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

    return max(dictionary, key=dictionary.get)

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
        
#CORRECT METHOD
# def most_common_character(my_string: str):

#     most_common = my_string[0]

#     for character in my_string:

#         if my_string.count(character) > my_string.count(most_common):

#             most_common = character

#     return most_common

# # Write your solution here