import random
import datetime

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.balance += amount
        self.transactions.append(
            f"Deposited: ₹{amount}"
        )
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.transactions.append(
            f"Withdrawn: ₹{amount}"
        )
        print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def show_transactions(self):
        print("\nTransaction History")

        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(transaction)

    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        return interest

    def add_interest(self, rate):
        interest = self.calculate_interest(rate)
        self.balance += interest
        self.transactions.append(
            f"Interest added: ₹{interest:.2f}"
        )
        print(f"Interest of ₹{interest:.2f} added.")


def generate_account_number():
    return random.randint(100000, 999999)


def display_menu():
    print("\n========== BANK MENU ==========")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Add Interest")
    print("6. Exit")
    print("=============================")


def main():
    print("Welcome to Python Bank!")

    name = input("Enter account holder name: ")

    account = BankAccount(name)

    account_number = generate_account_number()

    print(f"Your account number is: {account_number}")

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            rate = float(input("Enter interest rate: "))
            account.add_interest(rate)

        elif choice == "6":
            print("Thank you for using Python Bank!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

print("Hello")