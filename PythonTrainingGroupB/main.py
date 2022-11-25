# import pandas as pd
import json
from Portfolio import *

def load_accounts(path):
    f = open(path)
    return json.load(f)

def add_new_account(path, accounts, new_username, new_password):
    accounts[new_username] = new_password
    with open(path, 'w') as fp:
        json.dump(accounts, fp)

def login(accounts):
    print("Welcome to our Investment Game! If you want to sign up, press '0'. If you already have an account, press '1' to log in.")

    choice = int(input("Please make your choice: "))

    if choice == 0:
        login = new_login(accounts)
        return login
    elif choice == 1:
        login = existing_login(accounts)
        return login

def new_login(accounts):
    new_username = input("Please enter a username: ")
    while new_username in accounts:
        print("User name already exists, please enter another username: ")
        new_username = input("Please enter a username: ")
    new_password = input("Please enter a password: ")

    add_new_account('accounts.json', accounts, new_username, new_password)

    print("Registration completed")

    return new_username


def existing_login(accounts):
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








