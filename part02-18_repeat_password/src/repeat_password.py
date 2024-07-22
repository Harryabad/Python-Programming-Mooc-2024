# Write your solution here
pw = input("Password")
while True:
    rp = input("Repeat passowrd:")
    if rp != pw:
        print("They do not match!")
    elif rp == pw:
        print("User account created!")
        break