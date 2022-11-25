from Portfolio import *

def investing_choice_menu(user_name, portfolios):
    print(f"Welcome in the main menu user {user_name}! please type any of the options in the terminal to perform the listed actions.")

    print("========== Menu ==========")
    print("=     view portfolio     =")
    print("=     deposit  money     =")
    print("=     withdraw money     =")
    print("=       buy stocks       =")
    print("=      sell stocks       =")
    print("=      exit game         =")
    print("==========================")

    choice = input('Please type in the menu option:')

    if choice == "view portfolio":
        display_portfolio(user_name, portfolios)
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)
    elif choice == "deposit money":
        amount = int(input("How much money would you like to deposit to your balance?"))
        add_money(user_name, portfolios, amount)
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)
    elif choice == "withdraw money":
        amount = int(input("How much money would you like to withdraw from your balance?"))
        withdraw_money(user_name, portfolios, amount)
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)
    elif choice == "buy stocks":
        print("This functionality currently does not exist")
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)
    elif choice == "sell stocks":
        print("This functionality currently does not exist")
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)
    elif choice == "exit game":
        print("Exiting Investment Game, Thanks for playing")
    else:
        print("You did not type a valid menu choice")
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)

