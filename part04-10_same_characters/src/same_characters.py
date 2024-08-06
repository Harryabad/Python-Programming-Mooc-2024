# Write your solution here
def same_chars(text, index_a, index_b):

    if index_a < len(text) and index_b < len(text):
        if text[index_a] == text[index_b]:
            return True
        else:
            return False
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))