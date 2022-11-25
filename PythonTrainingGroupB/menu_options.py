from Portfolio import *
from sell_stock import sel_stock

def investing_choice_menu(user_name, portfolios):
    print(f"Welcome in the main menu user {user_name}! please type in the number of a menu option in the terminal to perform the action.")

    print("========== Menu ==========")
    print("=    1 view portfolio    =")
    print("=    2 deposit money     =")
    print("=    3 withdraw money    =")
    print("=    4 buy stocks        =")
    print("=    5 sell stocks       =")
    print("=    6  exit game        =")
    print("==========================")

    choice = input('Please type in the menu option number:')

    if int(choice) == 1:
        display_portfolio(user_name, portfolios)
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 2:
        amount = int(input("How much money would you like to deposit to your balance?"))
        add_money(user_name, portfolios, amount)
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 3:
        amount = int(input("How much money would you like to withdraw from your balance?"))
        withdraw_money(user_name, portfolios, amount)
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 4:
        print("This functionality currently does not exist")
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 5:
        sel_stock(user_name, portfolios)
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 6:
        print("Exiting Investment Game, Thanks for playing")
    else:
        print("You did not type a valid menu choice")
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)

