import json

def load_currencies(path):
    """"
    :param path: The name of the json file that serves as input.
    :return: This function returns the json file such that it can be used for data analysis.
    """

    f = open(path)
    return json.load(f)


def new_currency():
    valuta = None
    print("Please enter the valuta used by your bank.")
    print("------------------------------------------")
    user_input = int(input("\n 0: US Dollar \n 1: Euro \n 2: British Pound \n 3: Japanese Yen \n"))
    if user_input == 0:
        valuta = 'US Dollar'
    elif user_input == 1:
        valuta = 'Euro'
    elif user_input == 2:
        valuta = 'British Pound'
    elif user_input == 3:
        valuta = 'Japanese Yen'
    else:
        print("You entered invalid input")
    return valuta


def add_new_currency(path, username, currencies):
    """"
    add_new_currency creates a new entry in the json database for the used currency

    :param path: the path where we want to write the output to.
    :currencies: the json file of existing usernames and currencies that serves as input.
    :new_username: The username specified by the user.
    :valuta: The valuta specified by the user.
    :return: This function updates the json file with currency information of the new user.
    """

    currencies[username] = new_currency()
    with open(path, 'w') as fp:
        json.dump(currencies, fp)


