# Write your solution here

def palindromes(string):

    if string == string[::-1]:
        print(f"{string} is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        break

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
