from Portfolio import *

def investing_choice_menu(user_name, portfolios):
    print(f"Welcome in the main menu user {user_name}! please type any of the options in the terminal to perform the listed actions.")

    print("========== Menu ==========")
    print("=    1 view portfolio    =")
    print("=    2 deposit money     =")
    print("=    3 withdraw money    =")
    print("=    4 buy stocks        =")
    print("=    5 sell stocks       =")
    print("=    6  exit game        =")
    print("==========================")

    choice = input('Please type in the menu option:')

    if choice == "view portfolio" or int(choice) == 1:
        display_portfolio(user_name, portfolios)
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif choice == "deposit money" or int(choice) == 2:
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
    elif choice == "withdraw money" or int(choice) == 3:
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
    elif choice == "buy stocks" or int(choice) == 4:
        print("This functionality currently does not exist")
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif choice == "sell stocks" or int(choice) == 5:
        print("This functionality currently does not exist")
        return_choice = input("want to return to the menu? [yes, no]")
        if return_choice == "yes":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "no":
            print("Exiting Investment Game, Thanks for playing")
        else:
            print("not a valid answer, returning to main menu")
            investing_choice_menu(user_name, portfolios)
    elif choice == "exit game" or int(choice) == 6:
        print("Exiting Investment Game, Thanks for playing")
    else:
        print("You did not type a valid menu choice")
        print("You are now returning to the main menu")
        investing_choice_menu(user_name, portfolios)

