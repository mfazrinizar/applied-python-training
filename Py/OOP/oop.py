# OOP Exercises

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"Account holder: {self.firstname} {self.lastname}\nTotal Income: {self.total_income()}\nTotal Expense: {self.total_expense()}\nAccount Balance: {self.account_balance()}"

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def account_balance(self):
        return self.total_income() - self.total_expense()

# Testing the class and its functions
account = PersonAccount('Akmal', 'The Cat')
account.add_income('Salary', 10000)
account.add_income('Freelance', 1500)
account.add_expense('Rent', 1200)
account.add_expense('Groceries', 300)

print(account.account_info())
# Output:
# Account holder: John Doe
# Total Income: 6500
# Total Expense: 1500
# Account Balance: 5000