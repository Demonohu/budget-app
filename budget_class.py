"""
Goal: “Create a Budget class that can instantiate objects based on 
different budget categories like food, clothing, and entertainment. 
These objects should allow for depositing and withdrawing funds 
from each category, as well computing category balances and 
transferring balance amounts between categories”


Approach: define the purpose and flexibility of a class object; 
build its class methods using a modular approach and develop an 
understanding for how different instances of the same class can interact.
"""

class Budget:
    def __init__(self):
        """ Initialize the categories and the starting 
        budgets of each categories to 0. """
        self.category = ['food', 'entertainment', 'clothing']
        self.food_balance = 0
        self.entertainment_balance = 0
        self.clothing_balance = 0

    def deposit(self, amount, category):
        """ The deposit method; takes in the amount 
        and category, and adds it to the category balance.
        It prints an error message if the user puts a wrong category. """
        if category.lower() == 'food':
            self.food_balance += amount
        elif category.lower() == 'entertainment':
            self.entertainment_balance += amount
        elif category.lower() == 'clothing':
            self.clothing_balance += amount
        else:
            print("Wrong input.")

    def withdraw(self, amount, category):
        """ The withdraw method; takes in the amount and 
        category, checks if there is up to that amount in 
        the category  balance and removes the amount from 
        the balance if there's sufficient funds. It prints
        an error message if there's insufficient funds. """
        if category.lower() == 'food':
            if self.food_balance >= amount:
                self.food_balance -= amount
            else:
                print("You don't have the facilities for that, werey.")
        elif category.lower() == 'entertainment':
            if self.entertainment_balance >= amount:
                self.entertainment_balance -= amount
            else:
                print("You don't have the facilities for that, werey.")
        elif category.lower() == 'clothing':
            if self.clothing_balance >= amount:
                self.clothing_balance -= amount
            else:
                print("You don't have the facilities for that, werey.")

    def transfer(self, amount, sender, receiver):
        """ The transfer method; takes in the amount, 
        sender(category) and receiver(category), checks 
        if there's sufficient fund in the sender's balance and 
        transfers the amount to the receiver's balance if there's 
        sufficient funds. It prints an error message if otherwise. """
        if sender.lower() == 'food' and receiver.lower() == 'entertainment':
            if amount >= self.food_balance:
                self.food_balance -= amount
                self.entertainment_balance += amount
            else:
                print("You don't have the facilities for that, werey.")

        elif sender.lower() == 'food' and receiver.lower() == 'clothing':
            if amount >= self.food_balance:
                self.food_balance -= amount
                self.clothing_balance += amount
            else:
                print("You don't have the facilities for that, werey.")

        elif sender.lower() == 'entertainment' and receiver.lower() == 'food':
            if amount >= self.entertainment_balance:
                self.entertainment_balance -= amount
                self.food_balance += amount
            else:
                print("You don't have the facilities for that, werey.")

        elif sender.lower() == 'entertainment' and receiver.lower() == 'clothing':
            if amount >= self.entertainment_balance:
                self.entertainment_balance -= amount
                self.clothing_balance += amount
            else:
                print("You don't have the facilities for that, werey.")

        elif sender.lower() == 'clothing' and receiver.lower() == 'food':
            if amount >= self.clothing_balance:
                self.clothing_balance -= amount
                self.food_balance += amount
            else:
                print("You don't have the facilities for that, werey."
)
        elif sender.lower() == 'clothing' and receiver.lower() == 'entertainment':
            if amount >= self.clothing_balance:
                self.clothing_balance -= amount
                self.entertainment_balance += amount
            else:
                print("You don't have the facilities for that, werey.")

        else:
            print("Check wetin you input. You don make mistake.")

    def get_balance(self, category):
        """ The get balance method; takes in the category 
        and prints the balance. """
        if category.lower() == 'food':
            print('${:,.2f}'.format(self.food_balance))
        elif category.lower() == 'entertainment':
            print('${:,.2f}'.format(self.entertainment_balance))
        elif category.lower() == 'clothing':
            print('${:,.2f}'.format(self.clothing_balance))