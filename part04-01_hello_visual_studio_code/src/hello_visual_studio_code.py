# Write your solution here
while True:
    editor = input("Editor: ")

    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word":
        print("awful")
    else:
        print("not good")
