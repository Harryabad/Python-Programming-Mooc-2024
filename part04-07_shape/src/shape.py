# Copy here code of line function from previous exercise and use it in your solution
def line(count, text):
    if text == "":
        text = "*"
    print(text[0] * count)

def shape(t_height, t_character, s_height, s_character):


    i = 1
    while i <= t_height:
        line(i, t_character)
        i += 1

    j= 0
    while j < s_height:
        line(t_height, s_character)
        j += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")