from collections import defaultdict


def category_summary(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense.category] += expense.amount
    return summary


def monthly_report(expenses, month):
    total = 0
    count = 0

    for expense in expenses:
        if expense.date.startswith(month):
            total += expense.amount
            count += 1

    average = total / count if count else 0
    return total, average
