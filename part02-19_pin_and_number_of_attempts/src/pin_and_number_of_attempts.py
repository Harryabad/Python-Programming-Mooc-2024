# Write your solution here
correct_pin = 4321
count = 0
while True:
    pin = int(input("PIN: "))
    count += 1
    if pin != correct_pin:
        print("Wrong")
    else:
        if count == 1:
            print(f"Correct! It only took you one single attempt!")
            break
        print(f"Correct! It took you {count} attempts")
        break
