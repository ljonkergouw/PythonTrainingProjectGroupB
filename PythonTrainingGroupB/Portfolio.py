import json

with open('Portfolios.json', 'r') as j:
    portfolios = json.loads(j.read())

def get_portfolio(user_name):
    if user_name in [portfolio['username'] for portfolio in portfolios['users']]:
        return [portfolio for portfolio in portfolios['users'] if portfolio['username'] == user_name][0]['portfolio']
    else:
        print('Portfolio does not exist')

def display_portfolio(user_name):
    personal_portfolio = get_portfolio(user_name)

    print(f"Portfolio displayed for user {user_name}:")
    print(f"Your Portfolio contains {len(personal_portfolio['portfolio'])} stocks and your balance is €{personal_portfolio['balance']}!")

display_portfolio('luuk')

def add_money(user_name, amount):
    personal_portfolio = get_portfolio(user_name)
    balance = personal_portfolio['balance']
    if type(amount) == float or type(amount) == int and amount > 0:
        balance += amount
        print(f'Your balance is now {balance}')
        return balance
    else:
        print("The amount given is not a positive number!")

def change_balance(user_name, portfolios, amount):
    personal_portfolio = [portfolio for portfolio in portfolios['users'] if portfolio['username'] == user_name][0]

    user_index = [portfolio['username'] for portfolio in portfolios['users']].index(user_name)

    new_balance = add_money(user_name, amount)
    personal_portfolio['portfolio']['balance'] = new_balance

    portfolios[user_index] = personal_portfolio

    with open('portfolios.json', 'w') as fp:
        json.dump(portfolios, fp)



change_balance("luuk", portfolios, 5000)

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
