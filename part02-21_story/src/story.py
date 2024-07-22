# Write your solution here
string = ""
lastword = "."
while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    if lastword == word:
        break
    lastword = word
    string += word + " "
print(string)