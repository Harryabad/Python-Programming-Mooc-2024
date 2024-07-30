# Write your solution here
def line(count, text):
    if text == "":
        text = "*"
    print(text[0] * count)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")