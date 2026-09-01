print("="*45)
print("    Bank Account Management System")
print("="*45)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter your name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:
    print("=====BANK ACCOUNT MENU=====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice:"))

    if choice == 1:
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
