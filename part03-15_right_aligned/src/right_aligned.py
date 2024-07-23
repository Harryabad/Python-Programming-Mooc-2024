# Write your solution here
string = input("Please type in a string: ")
if len(string) < 20:
    print(f"*"*(20-len(string))+f"{string}")