# Write your solution here

def anagrams(string_a, string_b):

    return sorted(string_a) == sorted(string_b)

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True