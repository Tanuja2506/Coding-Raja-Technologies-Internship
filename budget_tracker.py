import json
from datetime import datetime

class BudgetTracker:
    def __init__(self, filename='transactions.json'):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as file:
                transactions = json.load(file)
            return transactions
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {'income': [], 'expenses': []}

    def save_transactions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=2)

    def add_income(self, category, amount):
        transaction = {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'category': category, 'amount': amount}
        self.transactions['income'].append(transaction)
        self.save_transactions()

    def add_expense(self, category, amount):
        transaction = {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'category': category, 'amount': amount}
        self.transactions['expenses'].append(transaction)
        self.save_transactions()

    def calculate_budget(self):
        income_total = sum(transaction['amount'] for transaction in self.transactions['income'])
        expenses_total = sum(transaction['amount'] for transaction in self.transactions['expenses'])
        remaining_budget = income_total - expenses_total
        return remaining_budget

    def expense_analysis(self):
        expenses_by_category = {}
        for transaction in self.transactions['expenses']:
            category = transaction['category']
            amount = transaction['amount']
            if category not in expenses_by_category:
                expenses_by_category[category] = amount
            else:
                expenses_by_category[category] += amount
        return expenses_by_category

    def display_summary(self):
        remaining_budget = self.calculate_budget()
        print("\nBudget Summary:")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

        expenses_by_category = self.expense_analysis()
        if expenses_by_category:
            print("\nExpense Analysis:")
            for category, amount in expenses_by_category.items():
                print(f"{category}: ${amount:.2f}")
        else:
            print("\nNo expenses recorded yet.")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Display Summary\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            budget_tracker.add_income(category, amount)
            print("Income recorded successfully.")

        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_expense(category, amount)
            print("Expense recorded successfully.")

        elif choice == '3':
            budget_tracker.display_summary()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
