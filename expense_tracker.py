import argparse
import json
import os

DATA_FILE = "data/expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(amount, category, date):
    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses(expenses)
    print(f"Added: {amount} in {category} on {date}")

def list_expenses(category=None):
    expenses = load_expenses()
    if category:
        expenses = [e for e in expenses if e["category"] == category]
    for e in expenses:
        print(f"{e['date']} | {e['category']:10} | {e['amount']}")

def main():
    parser = argparse.ArgumentParser(description="Simple Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", type=str, required=True)
    add_parser.add_argument("--date", type=str, required=True)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--category", type=str, default=None)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.amount, args.category, args.date)
    elif args.command == "list":
        list_expenses(args.category)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()