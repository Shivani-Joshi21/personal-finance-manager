from datetime import datetime


def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            print("Amount must be greater than 0")
            return None
        return amount
    except ValueError:
        print("Invalid amount")
        return None


def validate_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return None
