from Portfolio import *
from transactions import *
from search import *

def investing_choice_menu(user_name, portfolios):
    print(f"Welcome in the main menu user {user_name}! please type in the number of a menu option in the terminal to perform the action.")

    print("========== Menu ==========")
    print("=    1 view portfolio    =")
    print("=    2 deposit money     =")
    print("=    3 withdraw money    =")
    print("=    4 buy stocks        =")
    print("=    5 sell stocks       =")
    print("=    6 search            =")
    print("=    7 exit game         =")
    print("==========================")

    choice = input('Please type in the menu option number: ')

    if int(choice) == 1:
        display_portfolio(user_name, portfolios)
        return_choice = input("want to return to the menu? [y/n]: ")
        if return_choice == "y":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "n":
            print("Exiting Investment Game, Thanks for playing.")
        else:
            print("not a valid answer, returning to main menu.")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 2:
        amount = int(input("How much money would you like to deposit to your balance? "))
        add_money(user_name, portfolios, amount)
        return_choice = input("want to return to the menu? [y/n]: ")
        if return_choice == "y":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "n":
            print("Exiting Investment Game, Thanks for playing.")
        else:
            print("Not a valid answer, returning to main menu.")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 3:
        amount = int(input("How much money would you like to withdraw from your balance? "))
        withdraw_money(user_name, portfolios, amount)
        return_choice = input("Want to return to the menu? [y/n]: ")
        if return_choice == "y":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "n":
            print("Exiting Investment Game, Thanks for playing.")
        else:
            print("Not a valid answer, returning to main menu.")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 4:
        buy_stock(user_name, portfolios)
        return_choice = input("Want to return to the menu? [y/n]: ")
        if return_choice == "y":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "n":
            print("Exiting Investment Game, Thanks for playing.")
        else:
            print("Not a valid answer, returning to main menu.")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 5:
        sel_stock(user_name, portfolios)
        return_choice = input("want to return to the menu? [y/n]: ")
        if return_choice == "y":
            investing_choice_menu(user_name, portfolios)
        elif return_choice == "n":
            print("Exiting Investment Game, Thanks for playing.")
        else:
            print("Not a valid answer, returning to main menu.")
            investing_choice_menu(user_name, portfolios)
    elif int(choice) == 6:
        print('Search Menu')
        search_input = input("Please enter your search:")
        results = search(search_input)
        print_search_results(results)
        second_search = input("Of which of these stocks would you like to know more information? Please provide the ticker")
        stock_info(second_search, key)
        display_price_chart(second_search, key)
        print('Return to menu')
        investing_choice_menu(user_name, portfolios)
    elif int(choice) == 7:
        print("Exiting Investment Game, Thanks for playing.")
    else:
        print("You did not type a valid menu choice.")
        print("You are now returning to the main menu.")
        investing_choice_menu(user_name, portfolios)

