# Write your solution here

def shortest(my_list):

    shortest = float('inf')
    word = ""
    for i in my_list:
        if len(i) < shortest:
            shortest = len(i)
            word = i
    return word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)