# Write your solution here
word = input("Please type in a string: ")
count = len(word)
while count >= 0 :
    print(word[count:])
    count-=1