from src.expense import Expense
from src.file_manager import load_expenses, save_expenses
from src.utils import validate_amount, validate_date
from src.reports import category_summary, monthly_report
from src.menu import show_menu


expenses = load_expenses()

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        amount = validate_amount(input("Amount: "))
        if amount is None:
            continue
        category = input("Category: ")
        date = validate_date(input("Date (YYYY-MM-DD): "))
        if date is None:
            continue
        desc = input("Description: ")
        expenses.append(Expense(amount, category, date, desc))
        save_expenses(expenses)
        print("✅ Expense Added")

    elif choice == '2':
        for exp in expenses:
            print(exp)

    elif choice == '3':
        summary = category_summary(expenses)
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")

    elif choice == '4':
        month = input("Enter month (YYYY-MM): ")
        total, average = monthly_report(expenses, month)
        print("Total:", total)
        print("Average:", average)

    elif choice == '5':
        print("👋 Goodbye")
        break

    else:
        print("❌ Invalid choice")