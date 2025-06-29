import datetime

# Data structure to store transactions (in-memory)
transactions = []

def main():
    while True:
        print("\n--- Personal Budget Manager ---")
        print("1. Add Transaction (Income/Expense)")
        print("2. View Transactions")
        print("3. View Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction_prompt()
        elif choice == "2":
            view_transactions_prompt()
        elif choice == "3":
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            summary = generate_monthly_summary(month, year)
            print_summary(summary)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def add_transaction_prompt():
    try:
        trans_type = input("Enter type (income/expense): ").strip().lower()
        amount = float(input("Enter amount: "))
        description = input("Enter description: ").strip()
        category = input("Enter category: ").strip().capitalize()
        date = input("Enter date (YYYY-MM-DD): ")
        add_transaction(trans_type, amount, description, category, date)
        print("Transaction added successfully.")
    except ValueError:
        print("Invalid input. Please try again.")

def add_transaction(trans_type, amount, description, category, date):
    """Adds a transaction to the list of transactions."""
    transaction = {
        'type': trans_type,
        'amount': amount,
        'description': description,
        'category': category,
        'date': date
    }
    transactions.append(transaction)
    return True

def view_transactions(filter_by=None):
    """Returns all transactions or filters by category/date."""
    if filter_by:
        return [t for t in transactions if t['category'] == filter_by]
    return transactions

def view_transactions_prompt():
    filter_by = input("Filter by category (leave blank for all): ").strip().capitalize()
    filtered_transactions = view_transactions(filter_by if filter_by else None)

    if filtered_transactions:
        print("\n--- Transactions ---")
        for trans in filtered_transactions:
            print(f"{trans['date']} | {trans['type'].capitalize()} | {trans['amount']} | {trans['category']} | {trans['description']}")
    else:
        print("No transactions found.")

def generate_monthly_summary(month, year):
    """Generates a monthly summary including income, expenses, and savings."""
    total_income = 0
    total_expenses = 0

    for transaction in transactions:
        trans_date = datetime.datetime.strptime(transaction['date'], '%Y-%m-%d')
        if trans_date.month == int(month) and trans_date.year == int(year):
            if transaction['type'] == 'income':
                total_income += transaction['amount']
            elif transaction['type'] == 'expense':
                total_expenses += transaction['amount']

    savings = total_income - total_expenses
    summary = {
        'income': total_income,
        'expenses': total_expenses,
        'savings': savings
    }
    return summary

def print_summary(summary):
    """Prints the summary in a readable format."""
    print("\n--- Monthly Summary ---")
    print(f"Total Income: ${summary['income']:.2f}")
    print(f"Total Expenses: ${summary['expenses']:.2f}")
    print(f"Savings: ${summary['savings']:.2f}")

if __name__ == "__main__":
    main()
