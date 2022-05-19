#Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. 
#These objects should allow for depositing and withdrawing funds from each category, 
#as well computing category balances and transferring balance amounts between categories

class Budget():
    def __init__(self, balance):
        self.balance = balance 

    def __repr__(self):
        return f'Current balance is: {self.balance}'

    def current_balance(self):
        balance = self.balance 
        return (f'Your current balance is {balance}') 
        
    def deposit(self, money):
        self.balance = self.balance + money
        deposit_info = (f'You have deposited {money}, your new balance is {self.balance}')
        return deposit_info

    def withdraw(self, money):
        if self.balance < money:
            return (f'Not enough money in your account')
        else:
            self.balance = self.balance - money
            withdraw_info = (f'You have withdrawn {money}, your new balance is {self.balance}')
            return withdraw_info