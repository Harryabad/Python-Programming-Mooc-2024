# Write your solution here


while True:
    num = int(input("Please type in a number: "))
    fact = 1
    count = num

    if num <= 0:
        print("Thanks and bye!")
        break
    
    while count >0:
        fact *= count
        count -= 1
    print(f"The factorial of the number {num} is {fact}")
    
