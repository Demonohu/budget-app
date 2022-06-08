"""
Goal: “Create a Budget class that can instantiate objects based on 
different budget categories like food, clothing, and entertainment. 
These objects should allow for depositing and withdrawing funds 
from each category, as well computing category balances and 
transferring balance amounts between categories”


Approach: define the purpose and flexibility of a class object; 
build its class methods using a modular approach and develop an 
understanding for how different instances of the same class can interact.


I will be using dictionaries to do this.
"""

class Budget:
    def __init__(self):
        """Initialize the categories and their starting
        budgets to 0 using dictionaries."""
        self.categories = {'food':0, 'entertainment':0, 'clothing':0}

    def deposit(self, amount, category):
        """The deposit method takes in the amount to be deposited
        and category, and adds it to the category balance."""
        self.categories[category.lower()] += amount

    def withdraw(self, amount, category):
        """The withdraw method takes in the amount to be withdrawn and category, 
        and grants the withdraw request if there is sufficient funds.
        """
        try:
            if self.categories[category.lower()] >= amount:
                self.categories[category.lower()] -= amount
            else:
                print('Insufficient funds.')
        except KeyError:
            print('Incorrect details entered.')

    def transfer(self, amount, sender, receiver):
        """The transfer methods takes in the amount to be transferred,
        sender(category) and receiver(category) and grants the transfer
        request if there's sufficient funds."""
        if amount <= self.categories[sender.lower()]:
            self.categories[sender.lower()] -= amount
            self.categories[receiver.lower()] += amount
        elif amount >= self.categories[sender.lower()]:
            print('Insufficient funds.')
        else:
            print('Incorrect details entered.')

