# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")


while True:
    if len(word) == 0:
        break
    if (word[0] == character) and (len(word) >= 3):
        print(word[0 : 3])
    word = word[1:]