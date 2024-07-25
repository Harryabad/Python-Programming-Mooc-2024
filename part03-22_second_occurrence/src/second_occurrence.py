# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

while True:

    if len(string) == 0:
        break
    index = string.find(substring)
    string = string[index+(len(substring)):]

    if substring in string:

        index += string.find(substring) + len(substring)
        print(f"The second occurrence of the substring is at index {index}.")
        break
    else:
        print(f"The substring does not occur twice in the string.")
        break
        #test