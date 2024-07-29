# Write your solution here

def chessboard(num):
    i = 0
    while i < num:
        j = 0
        row = ""
        while j < num:
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
            j += 1
        print(row)
        i += 1





# Testing the function
if __name__ == "__main__":
    chessboard(3)
