from Portfolio import display_portfolio
import pandas as pd
import json
from currencies import get_currency
import requests
from Portfolio import display_portfolio, change_balance
from dateutil import parser
import datetime
import warnings
warnings.filterwarnings("ignore")

def buy_current_stock_price(company):
    dt = datetime.datetime.now()
    dt = str(dt)
    dt[:19]
    new = list(dt[:19])
    new[9] = '5'
    dt = ''.join(new)
    dt = parser.parse(dt)

    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&outputsize=full&apikey=AD3GLM6F3A21OGWC")
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code: ", response.status_code)
    raw_data = response.json()
    data = raw_data['Time Series (5min)']
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    df.index = pd.DatetimeIndex(df.index)
    idx = df.index[df.index.get_loc(dt, method='nearest')]
    stock_price = round(float(data[str(idx)]['2. high']), 2)

    return stock_price

def buy_stock(user, portfolios):

    display_portfolio(user, portfolios)

    print("From which company do you want to buy shares?")
    company = input("Please enter the company ticker: ")
    print("\n")

    table1 = pd.read_html('https://www.dividendmax.com/market-index-constituents/aex-25')
    table2 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table3 = pd.read_html('https://www.dividendmax.com/market-index-constituents/dax-40')

    df1 = table1[0]
    df2 = table2[0]
    df3 = table3[0]

    AEX = list(df1.Ticker)
    SP500 = list(df2.Symbol)
    DAX = list(df3.Ticker)

    if company not in AEX and company not in SP500 and company not in DAX:
        print(
            f"We currently do not support any transactions of {company}, we only support transaction of companies listed on the DAX, S&P500 & AEX")
        choice = input("Do you want to make another transation? [y/n]")
        if choice == 'y':
            buy_stock(user, portfolios)
        else:
            print("Returning to menu")
    else:

        buy_quantity = input("How many shares do you want to purchase? ")

        try:
            float(buy_quantity)
        except ValueError:
            print("This is not a number")
            buy_quantity = input("Enter a number ")
        print("\n")

        buy_quantity = float(buy_quantity)

        if buy_quantity <= 0:
            print("The amount you entered is invalid, please enter a valid number of shares.")
            choice = input("Would you like to try again [y/n]: ")
            if choice == 'y':
                buy_stock(user, portfolios)
            else:
                print("Back to menu.")

        stock_price = round(float(buy_current_stock_price(company)), 2)
        current_balance = portfolios['users'][user]['portfolio']['balance']
        currency = get_currency(company, "EMFE4N5TBX48Y6W5")

        if currency == 'EUR':
            stock_price = stock_price / 1.04
        else:

            if current_balance - (stock_price * buy_quantity) < 0:
                print(
                    f"Your funds are insufficient. In order to complete this transaction, please increase your balance by {abs(current_balance - (stock_price * buy_quantity))}")
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
                    print("Ending: back to menu.")
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
                    portfolios['users'][user]['portfolio']['balance'] = round(new_balance, 4)

                    with open("Portfolios.json", 'w') as fp:
                        json.dump(portfolios, fp)

                    # transaction receipt
                    print("Transaction completed.")
                    print("---------------------------------------------")
                    print(f"Shares bought: {buy_quantity}")
                    print(f"Company: {company}")
                    print(f"Total amount: {stock_price * buy_quantity}")
                    print(f"Currency: EUR")  # here the currency needs to be added
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

def sell_current_stock_price(company):
    dt = datetime.datetime.now()
    dt = str(dt)
    dt[:19]
    new = list(dt[:19])
    new[9] = '5'
    dt = ''.join(new)
    dt = parser.parse(dt)

    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&outputsize=full&apikey=AD3GLM6F3A21OGWC")
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)
    raw_data = response.json()
    data = raw_data['Time Series (5min)']
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    df.index = pd.DatetimeIndex(df.index)

    idx = df.index[df.index.get_loc(dt, method='nearest')]
    stock_price = round(float(data[str(idx)]['3. low']), 2)

    return stock_price


def sel_stock(user, portfolios):
    # display portfolio
    print("Your current portfolio is: ")
    display_portfolio(user, portfolios)

    print("From which company do you want to sell shares?")
    company = input("Please enter the company ticker: ")
    print("\n")

    if company not in portfolios['users'][user]['portfolio']['stocks']:
        print("The company that you selected is not in your portfolio, please select another company.")

        print("Do you want to continue?")
        choice = input("Please enter [y/n]: ")
        print("\n")

        while choice == "y":
            sel_stock(user, portfolios)

        if choice == "n":
            print("You will return to the menu.")
            print("\n")

    else:

        print("How many shares do you want to sell?")
        sell_quantity = float(input("Please enter the amount of shares: "))
        print("\n")

        if sell_quantity <= 0:
            print("The amount you entered is invalid, please enter a valid number of shares.")
            choice = input("Would you like to try again [y/n]: ")
            if choice == 'y':
                sel_stock(user, portfolios)
            else:
                print("Back to menu.")

            # vars to make code more readable
        current_quantity = portfolios['users'][user]['portfolio']['stocks'][company]['quantity']

        current_balance = portfolios['users'][user]['portfolio']['balance']
        stock_price = round(float(sell_current_stock_price(company)), 4)
        currency = get_currency(company, "EMFE4N5TBX48Y6W5")
        if currency == 'EUR':
            pass
        else:
            if sell_quantity > current_quantity:
                print(
                    f"You do not have that many shares in your possession, you currently have {current_quantity} shares of {company}")
                print("\n")

                print("Do you want to continue?")
                choice = input("Please enter [y/n]: ")
                print("\n")

                while choice == "y":
                    sel_stock(user, portfolios)
                if choice == "n":
                    print("You will return to the menu")
                    print("\n")

            if sell_quantity <= current_quantity:
                print(
                    f"thank you, are you sure that you want to sell {sell_quantity} of {company} at the current price of {stock_price}?")
                choice = input("please confirm [y/n]: ")
                print("\n")

                if choice == "y":
                    test = "a"

                    # update balance
                    balance = portfolios['users'][user]['portfolio']['balance'] + (stock_price * sell_quantity)
                    change_balance(user, portfolios, balance)
                    print(
                        f"Transaction SELL of {sell_quantity} shares {company} with a total amount of {stock_price * sell_quantity} EURO completed")  # here the currency needs to be added
                    print("\n")

                    # update quantity
                    portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] = (
                            portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] - sell_quantity)
                    if portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] == 0:
                        del portfolios['users'][user]['portfolio']['stocks'][company]

                    with open("Portfolios.json", 'w') as fp:
                        json.dump(portfolios, fp)

                    # display portfolio
                    print("Your current portfolio after transaction is: ")
                    display_portfolio(user, portfolios)

                elif choice == "n":
                    print("Do you want to continue?")
                    choice = input("please enter [y/n]: ")
                    print("\n")
                    while choice == "y":
                        sel_stock(user, portfolios)
                    if choice == "n":
                        print("You will return to the menu.")
                        print("\n")

    return portfolios