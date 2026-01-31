import csv
import os
from src.expense import Expense

DATA_FILE = "data/expense.csv"


def load_expenses():
    expenses = []

    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        for row in reader:
            date, category, amount, description = row
            expenses.append(Expense(amount, category, date, description))

    return expenses


def save_expenses(expenses):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for expense in expenses:
            writer.writerow(expense.to_list())
