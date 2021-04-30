class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return f"You have successfully deposited {amount} in {self.category} category"

    def category_balance(self):
        return f"The current balance allotted to {self.category} is: {self.amount}"

    def check_balance(self, amount):
        if amount > self.amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.amount -= amount
        return f"You have successfully withdrawn {amount} in {self.category} category"

    def transfer(self, amount, category):
        if self.check_balance(amount):
            self.withdraw(amount)
            category.deposit(amount)
            print(f"You have successfully transferred {amount} from {self.category} to {category.category}")
            return True
        else:
            return False
