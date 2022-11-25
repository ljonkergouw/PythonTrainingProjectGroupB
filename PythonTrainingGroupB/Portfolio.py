import json

def load_portfolios(path):
    with open('Portfolios.json', 'r') as j:
        portfolios = json.loads(j.read())
    return portfolios

def get_portfolio(user_name, portfolios):
    if user_name in [portfolio['username'] for portfolio in portfolios['users']]:
        return [portfolio for portfolio in portfolios['users'] if portfolio['username'] == user_name][0]
    else:
        print('Portfolio does not exist')
def display_portfolio(user_name, portfolios):
    personal_portfolio = get_portfolio(user_name, portfolios)

    print(f"Portfolio displayed for user {user_name}:")

    print(f"Your Portfolio contains {len(personal_portfolio['portfolio'])} stocks and your balance is €{personal_portfolio['portfolio']['balance']}!")

def add_money(user_name, portfolios, amount):
    personal_portfolio = get_portfolio(user_name, portfolios)

    balance = get_balance(user_name)

    if type(amount) == float or type(amount) == int and amount > 0:
        new_balance = balance + amount
        change_balance(user_name, portfolios, new_balance)
        print(f"{amount} is added to your initial balance of {balance} so your new balance is now {personal_portfolio['portfolio']['balance']}")
        return balance
    else:
        print("The amount given is not a positive number!")

def change_balance(user_name, portfolios, new_balance):
    print(portfolios)
    personal_portfolio = get_portfolio(user_name, portfolios)
    personal_portfolio['portfolio']['balance'] = new_balance

    print(portfolios)
    with open('portfolios.json', 'w') as fp:
        json.dump(portfolios, fp)

def get_balance(user_name):
    return get_portfolio(user_name, portfolios)['portfolio']['balance']

def withdraw_money(user_name, portfolios, amount):
    personal_portfolio = get_portfolio(user_name, portfolios)

    balance = get_balance(user_name)

    if amount > balance:
        print("You are trying to withdraw more money than is currently in your balance!")
        print("Please provide an amount which is less or equal to your balance")

    elif type(amount) == float or type(amount) == int and amount > 0:
        new_balance = balance - amount
        change_balance(user_name, portfolios, new_balance)
        print(f"Your balance is now {personal_portfolio['portfolio']['balance']}")
    else:
        print("The amount given is not a positive number!")

def check_if_portfolio_exists(portfolios, user_name):
    if user_name not in [portfolio['username'] for portfolio in portfolios['users']]:
        choice = input('It seems you do not have a portfolio, want to create one? [yes, no]')
        if choice == "yes":
            create_empty_portfolio(portfolios, user_name)
    else:
        choice = input(f'Welcome back user {user_name}, want see how your portfolio is doing? [yes, no]')
        if choice == "yes":
            display_portfolio(user_name, portfolios)


def create_empty_portfolio(portfolios, user_name):
    if user_name not in [portfolio['username'] for portfolio in portfolios['users']]:
        portfolios['users'].append({'username': user_name, 'portfolio':{'balance' : 0, 'stocks' : {}}})
        with open('portfolios.json', 'w') as fp:
            json.dump(portfolios, fp)
        print('Empty portfolio created')
        display_portfolio(user_name, portfolios)
    else:
        print('This username already exists, please create a portfolio with a different username!')


if __name__ == '__main__':
    portfolios = load_portfolios('Portfolios.json')
    add_money("luuk", portfolios, 5000)
    display_portfolio('luuk', portfolios)
    create_empty_portfolio(portfolios, "luuk")
    withdraw_money('luuk', portfolios, 50000)
