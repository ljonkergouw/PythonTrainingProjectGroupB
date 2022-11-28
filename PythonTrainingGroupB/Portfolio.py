import json

def load_portfolios(path):
    """
    load_portfolios loads in the users portfolios from a json file

    :param path: the path to the json file
    :return: a dictionary with the portfolio's
    """
    with open('Portfolios.json', 'r') as j:
        portfolios = json.loads(j.read())
    return portfolios

def get_portfolio(user_name, portfolios):
    """
    get_portfolio retrieves the portfolio of a single user from the portfolios dictionary

    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    :return: a dictionary with only the portfolio dictionary items of a single user
    """
    if user_name in portfolios['users'].keys():
        return portfolios['users'][user_name]
    else:
        print('Portfolio does not exist')

def get_user_currency(user_name):
    with open('currencies.json', 'r') as j:
        user_currencies = json.loads(j.read())

    return user_currencies[user_name]



def display_portfolio(user_name, portfolios):
    """
    display_portfolio shows the balance, the number of stocks, and the stocks a user has

    :param user_name: the username of a user
    :param portfolios: the portfolios dictionary
    """
    personal_portfolio = get_portfolio(user_name, portfolios)

    if get_user_currency(user_name) == 'EUR':

        print('Europath')

        print(f"Portfolio displayed for user {user_name}:")
        print(f"Your Portfolio contains {len(personal_portfolio['portfolio']['stocks'])} stocks and your balance is €{round(personal_portfolio['portfolio']['balance'], 4)}!")
        if len(personal_portfolio['portfolio']['stocks']) > 0:
            print('Stock \t\t Currency \t Price \t\t\t Quantity')
            print('----------------------------------------------------------------------------')
            for stock in personal_portfolio['portfolio']['stocks'].keys():
                print(
                    f"{stock} \t\t EUR \t\t {round(personal_portfolio['portfolio']['stocks'][stock]['price'] /1.04, 4)} \t\t {personal_portfolio['portfolio']['stocks'][stock]['quantity']}")


    else:
        print(f"Portfolio displayed for user {user_name}:")
        print(f"Your Portfolio contains {len(personal_portfolio['portfolio']['stocks'])} stocks and your balance is €{personal_portfolio['portfolio']['balance']}!")
        if len(personal_portfolio['portfolio']['stocks']) > 0:
            print('Stock \t\t Currency \t Price \t\t\t Quantity')
            print('----------------------------------------------------------------------------')
            for stock in personal_portfolio['portfolio']['stocks'].keys():
                print(f"{stock} \t\t USD \t\t {personal_portfolio['portfolio']['stocks'][stock]['price']} \t\t {personal_portfolio['portfolio']['stocks'][stock]['quantity']}")

def add_money(user_name, portfolios, amount):
    """
    with add_money a user can deposit money into the balance of the portfolio of the user

    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    :param amount: the amount
    """
    personal_portfolio = get_portfolio(user_name, portfolios)

    balance = get_balance(user_name, portfolios)

    if type(amount) == float or type(amount) == int and amount > 0:
        new_balance = balance + amount
        change_balance(user_name, portfolios, new_balance)
        print(f"{amount} is added to your initial balance of {balance} so your new balance is now {personal_portfolio['portfolio']['balance']}")
    else:
            print("The amount given is not a positive number!")


def change_balance(user_name, portfolios, new_balance):
    """
    change_balance is a helper-function of add_money and withdraw_money and performs the transaction in the portfolio.json file

    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    :param new_balance: the balance after money is added or withdrawn
    """
    personal_portfolio = get_portfolio(user_name, portfolios)
    personal_portfolio['portfolio']['balance'] = new_balance

    with open('portfolios.json', 'w') as fp:
        json.dump(portfolios, fp)

def get_balance(user_name, portfolios):
    """
    get_balance retrieves the balance from a user by searching in portfolios

    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    :return balance: the balance of a user
    """
    return get_portfolio(user_name, portfolios)['portfolio']['balance']

def withdraw_money(user_name, portfolios, amount):
    """
    with withdraw_money a user can withdraw money from the balance of the portfolio of the user

    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    :param amount: the amount
    """
    personal_portfolio = get_portfolio(user_name, portfolios)

    balance = get_balance(user_name, portfolios)

    if amount > balance:
        print("You are trying to withdraw more money than is currently in your balance!")
        print("Please provide an amount which is less or equal to your balance")

    elif type(amount) == float or type(amount) == int and amount > 0:
        new_balance = balance - amount
        change_balance(user_name, portfolios, new_balance)
        print(f"Your balance is now {personal_portfolio['portfolio']['balance']}")
    else:
        print("The amount given is not a positive number!")

def check_if_portfolio_exists(user_name, portfolios):
    """
    check_if_portfolio_exists checks if a user already has a portfolio and if not it calls
    create_empty_portfolio to create a new portfolio

    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    """
    if user_name not in portfolios['users'].keys():
        choice = input('It seems you do not have a portfolio, want to create one? [yes, no]')
        if choice == "yes":
            create_empty_portfolio(portfolios, user_name)
    else:
        print(f'Welcome back user {user_name}!')


def create_empty_portfolio(portfolios, user_name):
    """
    create_empty_portfio creates an empty portfolio for a user when the user does not have a portfolio
    :param user_name: the user_name of a user
    :param portfolios: the portfolios dictionary
    """
    if user_name not in portfolios['users'].keys():
        portfolios['users'][user_name] =  {'portfolio': {'balance': 0, 'stocks': {}}}
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
    #create_empty_portfolio("luuk", portfolios)
    #withdraw_money('luuk', portfolios, 50000)
    user_currency = get_user_currency('luuk')
    print(user_currency)
    display_portfolio('tjappie', portfolios)
