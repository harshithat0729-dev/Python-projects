print("===== PERSONAL EXPENSE CALCULATOR =====")

income = float(input("Enter your monthly income: ₹"))

food = float(input("Enter food expense: ₹"))
travel = float(input("Enter travel expense: ₹"))
shopping = float(input("Enter shopping expense: ₹"))
other = float(input("Enter other expense: ₹"))

total_expenses = food + travel + shopping + other
remaining_amount = income - total_expenses

print("\n----- EXPENSE SUMMARY -----")
print(f"Monthly Income: ₹{income}")
print(f"Total Expenses: ₹{total_expenses}")
print(f"Remaining Amount: ₹{remaining_amount}")

if remaining_amount >= 5000:
    print("Good savings!")
elif remaining_amount > 0:
    print("You have some amount left.")
else:
    print("Expenses exceeded your income.")

print("=" * 45)
