# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    index = word.find(character)
    if index >= 0 and index+3 < len(word):
        print(word[index:index+3])
    break