# Write your solution here
word = input("Word: ")
gap = ((28 - len(word))//2)


print("*"*30)
if len(word) %2 == 0:
    print(f"*"+f" "*(gap)+f"{word}"+f" "*(gap)+f"*")
else:
    print(f"*"+f" "*(gap)+f"{word}"+f" "*(gap+1)+f"*")

print("*"*30)