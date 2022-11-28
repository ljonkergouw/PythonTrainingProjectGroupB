from sell_stock import current_stock_price
from Portfolio import display_portfolio
import pandas as pd
import json

def buy_stock(user, portfolios):
    # load valid tickers
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    valid_tickers = list(df.Symbol)

    display_portfolio(user, portfolios)

    print("From which company do you want to buy shares?")
    company = input("Please enter the company ticker: ")
    print("\n")

    if company not in valid_tickers:
        print("This is an invalid ticker.")
        print("\n")
        print("")
        choice = input("Do you want to try again? [y/n]: ")
        if choice == 'y':
            buy_stock()
        else:
            print("Back to menu")
            print("\n")

    else:
        buy_quantity = float(input("How many shares do you want to purchase? "))
        print("\n")

        if buy_quantity <= 0:
            print("The amount you entered is invalid, please enter a valid number of shares.")
            choice = input("Would you like to try again [y/n]: ")
            if choice == 'y':
                buy_stock(user, portfolios)
            else:
                print("Back to menu")


        stock_price = float(current_stock_price(company))
        current_balance = portfolios['users'][user]['portfolio']['balance']

        if current_balance - (stock_price * buy_quantity) < 0:
            print(
                f"your funds are insufficient. In order to complete this transaction, please increase your balance by {abs(current_balance - (stock_price * buy_quantity))}")
            choice = input("Do you want to make a deposit [y/n]? ")
            if choice == 'y':
                print("Go make a deposit.")
            if choice == 'n':
                print("Go to menu.")
        else:
            print(
                f"Are you sure you want to buy {buy_quantity} of {company} for a total amount of {buy_quantity * stock_price}?")
            choice = input("Please enter [y/n]: ")
            print("\n")
            if choice == 'n':
                print("Ending: back to menu")
                print("\n")
            if choice == 'y':
                new_balance = portfolios['users'][user]['portfolio']['balance'] - (buy_quantity * stock_price)

                # check if stock is already in portfolio
                if company in portfolios['users'][user]['portfolio']['stocks']:
                    portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] += buy_quantity
                else:
                    portfolios['users'][user]['portfolio']['stocks'][company] = {'quantity': buy_quantity,
                                                                                 'price': stock_price}

                # updating current balance and stock qty in portfolio
                portfolios['users'][user]['portfolio']['balance'] -= new_balance

                with open("Portfolios.json", 'w') as fp:
                    json.dump(portfolios, fp)

                # transaction receipt
                print("Transaction completed.")
                print("---------------------------------------------")
                print(f"Shares bought: {buy_quantity}")
                print(f"Company: {company}")
                print(f"Total amount: {stock_price * buy_quantity}")
                print(f"Currency: EURO")  # here the currency needs to be added
                print("\n")

                # current portfolio
                print("Portfolio after transaction: ")
                display_portfolio(user, portfolios)

                choice = input("Do you want to continue [y/n]? ")
                if choice == 'y':
                    buy_stock(user, portfolios)
                else:
                    print("Back to menu.")
                    print("\n")


    return portfolios