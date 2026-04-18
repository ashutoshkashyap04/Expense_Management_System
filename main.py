#Expense Management System
import csv
import os 
from datetime import datetime 

FILE_NAME = "expenses.csv"
FIELDS = ["date", "amount", "Category", "payment_method", "description"]


class Expense:

    def __init__(self, date, amount,  category, payment_method, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.payment_method = payment_method
        self.description = description

    def to_list(self):
        return [self.date, self.amount, self.category, self.payment_method, self.description]

    def display_expense(self, index = None):
        prefix = f"{index}. " if index is not None else ""
        print(f"{prefix} Date: {self.date} | Amount: {self.amount} | Category: {self.category} | Payment Method: {self.payment_method}|  Description: {self.description}") 


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
                expenses.append(Expense(**row))
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


if __name__ == "__main__":
    def Menu_display():
        print("Expense Management System")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Reset Expenses")
        print("4. Update Expenses")
        print("5. Exit")        

    while True:
        Menu_display()
        choice = int(input("Enter your choice: "))


        if choice == 1:
            date = input("Enter date (DD-MM-YYYY): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category(e.g., Food, Transport, Utilities , Shopping): ")
            payment_method = input("Enter payment method (e.g., Cash, Credit Card, UPI): ")
            description = input("Enter description: ")
            expense = Expense(date, amount, category, payment_method, description)
            with open("expenses.csv", "a") as file:
                file.write(f"{date},{amount},{category},{payment_method},{description}\n")
                print("Expense added successfully!")


        elif choice == 2:
            print("Expenses:")
            try:
                with open('expenses.csv', 'r') as file:
                    for line in file:
                        date, amount, category, payment_method, description = line.strip().split(',')
                        expense = Expense(date, float(amount), category, payment_method, description)
                        expense.display_expense()
            except FileNotFoundError:
                print("No expenses recorded yet.")


        elif choice == 3:
            confirmation = input("Are you sure you want to reset all expenses? (YES/NO): ")
            if confirmation.upper() == "YES":
                open("expenses.csv", "w").close()
                print("All expenses have been reset.")
            else:
                print("Reset operation cancelled.")


        elif choice == 4:
            print("Showing current expenses: ")
            
            for i, line in enumerate(open('expenses.csv', 'r').readlines()):
                print(f"{i+1} -> {line.strip()}")


            line_number_to_update=int(input("Enter the line number of the expense to update (starting from 1): "))
            lines = open('expenses.csv', 'r').readlines()

            columns=lines[line_number_to_update - 1].strip().split(',')
            print("1.Date  , 2.Amount  , 3.Category  , 4.Payment Method  , 5.Description")
            column_number_to_update=int(input("Enter the column number to update(1-5): "))

            new_value=input("Enter the new value: ")
            columns[column_number_to_update - 1] = new_value

            lines[line_number_to_update - 1] = ','.join(columns) + '\n'

            with open('expenses.csv', 'w') as file:
                file.writelines(lines)

            print("Expense updated successfully!")

            


        elif choice == 5:
            print("Exiting the program.")
            break