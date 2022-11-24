import json

with open('Portfolios.json', 'r') as j:
    portfolios = json.loads(j.read())

def get_portfolio(user_name):
    if user_name in [portfolio['username'] for portfolio in portfolios]:
        print([portfolio for portfolio in portfolios if portfolio['username'] == user_name][0]['portfolio'])
    else:
        print('Portfolio does not exist')

get_portfolio('luuk')

def display_portfolio(self):
    print(f"Portfolio displayed for user {self.user_id}:")
    print(f'Your Portfolio contains {self.portfolio_count} stocks and your balance is €{self.balance}!')

def add_money(self, amount):
    if type(amount) == float or type(amount) == int and amount > 0:
        self.balance += amount
        print(f'Your balance is now {self.balance}')
    else:
        print("The amount given is not a positive number!")

def withdraw_money(self, amount):
    if amount > self.balance:
        print("You are trying to withdraw more money than is currently in your balance!")
        print("Please provide an amount which is less or equal to your balance")

    elif type(amount) == float or type(amount) == int and amount > 0:
        print(f"{amount} is deducted from your balance which is {self.balance}")
        self.balance -= amount
        print(f'Your balance is now {self.balance}')
    else:
        print("The amount given is not a positive number!")
