# Write your solution here
days = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure")
print(f"Daily: {((days * lunch) + groceries)/7} euros")
print(f"Weekly: {(days * lunch) + groceries} euros")