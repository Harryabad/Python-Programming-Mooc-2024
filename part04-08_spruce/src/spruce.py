# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    j = 1
    while i <= size:
        print(" " * (size-i) + ("*"*j))
        i+=1
        j+=2

    base = (size-1) * " " 
    print(base + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(4)