#Expense Management System
import csv
import os 
from datetime import datetime 

FILE_NAME = "expenses.csv"
FIELDS = ["date", "amount", "category", "payment_method", "description"]


class Expense:

    def __init__(self, date, amount,  category, payment_method, description):
        self.date = date
        self.amount = float(amount)
        self.category = category
        self.payment_method = payment_method
        self.description = description

    def to_list(self):
        return [self.date, self.amount, self.category, self.payment_method, self.description]

    def display_expense(self, index = None):
        prefix = f"{index}. " if index is not None else ""
        print(f"{prefix} Date: {self.date} | Amount: ₹{self.amount} | Category: {self.category} | Payment Method: {self.payment_method}|  Description: {self.description}") 


#File handling

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode = 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)

def read_expenses():
    expenses = []
    try:
        with open(FILE_NAME, mode = 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(
                    Expense(
                        row["date"],
                        float(row["amount"]),
                        row["category"],
                        row["payment_method"],
                        row["description"]
                        )
                    )
    except FileNotFoundError:
        print("File not found. Initializing new file...")
        initialize_file()
    return expenses 


def write_expenses(expenses):
    with open(FILE_NAME, mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(FIELDS)
        for exp in expenses:
            writer.writerow(exp.to_list())


# ----------Features -------------

def add_expense():
    try:
        date = input("Enter date (DD-MM-YYYY): ")
        datetime.strptime(date, "%d-%m-%Y")      #validate date

        amount = float(input("Enter amount: "))
        category = input("Enter category(Shopping, travel, etc): ")
        payment_method = input("Enter Payment method: ")
        description = input("Enter description: ")

        expense = Expense(date, amount, category, payment_method, description)

        expenses = read_expenses()
        expenses.append(expense)
        write_expenses(expenses)

        print("✅ Expense added successfully!")

    except ValueError:
        print("❌ Invalid input. Please try again.")


def view_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")
    for i, exp in enumerate(expenses, start=1):
        exp.display(i)

    total = sum(exp.amount for exp in expenses)
    print(f"\nTotal : ₹{total}")


def reset_expenses():
    confirm = input("Are you sure? (YES/NO): ")
    if confirm.upper() == "YES":
        initialize_file()
        print("✅ All expenses reset.")
    else:
        print("Cancelled.")

def update_expense():
    expenses = read_expenses()

    if not expenses:
        print("No expenses to update.")
        return

    print("\n--- Select Expense ---")
    for i, exp in enumerate(expenses, start=1):
        exp.display(i)

    try:
        idx = int(input("Enter expense number: ")) - 1
        if idx < 0 or idx >= len(expenses):
            print("Invalid selection.")
            return

        exp = expenses[idx]

        print("\nWhat do you want to update?")
        print("1. Date")
        print("2. Amount")
        print("3. Category")
        print("4. Payment Method")
        print("5. Description")

        choice = int(input("Enter choice: "))
        new_value = input("Enter new value: ")

        if choice == 1:
            datetime.strptime(new_value, "%d-%m-%Y")
            exp.date = new_value
        elif choice == 2:
            exp.amount = float(new_value)
        elif choice == 3:
            exp.category = new_value
        elif choice == 4:
            exp.payment_method = new_value
        elif choice == 5:
            exp.description = new_value
        else:
            print("Invalid choice.")
            return

        write_expenses(expenses)
        print("✅ Expense updated successfully!")

    except ValueError:
        print("❌ Invalid input.")


# -------------------- MENU --------------------
def show_menu():
    print("\n====== Expense Management System ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Reset Expenses")
    print("5. Exit")


def main():
    initialize_file()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                update_expense()
            elif choice == 4:
                reset_expenses()
            elif choice == 5:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice.")

        except ValueError:
            print("❌ Please enter a valid number.")


if __name__ == "__main__":
    main()
