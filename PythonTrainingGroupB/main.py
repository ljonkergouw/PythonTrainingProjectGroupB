# import pandas as pd
import json
from Portfolio import *

def load_accounts(path):
    """"
    :param path: The name of the json file that serves as input.
    :return: This function returns the json file such that it can be used for data analysis.
    """

    f = open(path)
    return json.load(f)

def add_new_account(path, accounts, new_username, new_password):
    """"
    add_new_account creates a new entry in the json database for new users with their username and the password.

    :param path: the path where we want to write the output to.
    :accounts: the json file of existing accounts that serves as input.
    :new_username: The username specified by the user.
    :new_password: The password specified by the user.
    :return: This function updates the json file with account information of the new user.
    """

    accounts[new_username] = new_password
    with open(path, 'w') as fp:
        json.dump(accounts, fp)

def login(accounts):
    """
    login asks the user whether they want to sign up, or want to log in to their existing account.

    :param accounts: the json file of existing accounts.
    :return: This returns the username of the new or existing user.
    """

    print("Welcome to our Investment Game! If you want to sign up, press '0'. If you already have an account, press '1' to log in.")

    choice = int(input("Please make your choice: "))

    if choice == 0:
        login = new_login(accounts)
        return login
    elif choice == 1:
        login = existing_login(accounts)
        return login

def new_login(accounts):
    """"
    new_login asks the user for a username and password, which will be documented in the system.

    :param accounts: the json file of existing accounts.
    :return: This returns the new username.
    """

    new_username = input("Please enter a username: ")
    while new_username in accounts:
        print("User name already exists, please enter another username: ")
        new_username = input("Please enter a username: ")
    new_password = input("Please enter a password: ")

    add_new_account('accounts.json', accounts, new_username, new_password)

    print("Registration completed")

    return new_username


def existing_login(accounts):
    """"
    exisiting_login asks the user for its username and password, in order to log in.

    :param accounts: the json file of existing accounts.
    :return: This returns the existing username.
    """

    print("Please enter you username.")

    while True:
        existing_username = input("Username: ")
        if existing_username in accounts:
            existing_password = input("Please enter your password: ")
            if existing_password == accounts[existing_username]:
                print("Log in succesful")
                return existing_username
                break
            else:
                print("You entered the wrong username/password combination. Please try again.")
        else:
            print("You didn't enter an existing username. Please try again ")

if __name__ == "__main__":
    accounts = load_accounts("accounts.json")
    user_name = login(accounts)
    portfolios = load_portfolios("Portfolios.json")
    check_if_portfolio_exists(portfolios, user_name)








