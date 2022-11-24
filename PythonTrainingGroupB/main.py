# from User import UserName
# import pandas as pd
import json

f = open("accounts.json")
accounts = json.load(f)

print("Welcome to our Investment Game! If you want to sign up, press '0'. If you already have an account, press '1' to log in.")

choice = int(input("Please make your choice: "))

if choice == 0:
    new_username = input("Please enter a username: ")
    while new_username in accounts:
        print("User name already exists, please enter another username: ")
        new_username = input("Please enter a username: ")
    new_password = input("Please enter a password: ")

    print("Registration completed")

    accounts[new_username] = new_password
    with open('accounts.json', 'w') as fp:
        json.dump(accounts, fp)

elif choice == 1:
    print("Please enter you username.")

    while True:
        existing_username = input("Username: ")
        if existing_username in accounts:
            existing_password = input("Please enter your password: ")
            if existing_password == accounts[existing_username]:
                print("Log in succesful")
                break
            else:
                print("You entered the wrong username/password combination. Please try again.")
        else:
            print("You didn't enter an existing username. Please try again ")








