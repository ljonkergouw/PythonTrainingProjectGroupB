import json
import requests
key = "EMFE4N5TBX48Y6W5"

def load_currencies(path):
    """"
    :param path: The name of the json file that serves as input.
    :return: This function returns the json file such that it can be used for data analysis.
    """

    f = open(path)
    return json.load(f)


def new_currency():
    """"
    new_currency asks the user for its valuta.
    """

    valuta = None
    print("Please enter the valuta used by your bank.")
    print("------------------------------------------")
    user_input = int(input("\n 0: US Dollar \n 1: Euro \n"))
    if user_input == 0:
        valuta = 'USD'
    elif user_input == 1:
        valuta = 'EUR'
    else:
        print("You entered invalid input")
    return valuta


def add_new_currency(path, currencies, username):
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

def get_currency(symbol, key):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    return data['Currency']


if __name__ == "__main__":
    currency = get_currency("AAPL", key=key)
    print(currency)



