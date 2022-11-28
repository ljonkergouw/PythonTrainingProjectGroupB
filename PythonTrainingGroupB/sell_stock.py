import requests
import json
from Portfolio import display_portfolio


def current_stock_price(company):
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&outputsize=full&apikey=AD3GLM6F3A21OGWC")
    raw_data = response.json()
    price_data = raw_data['Time Series (5min)']
    recent_key = list(price_data.keys())[:1]
    stock_price = (float(price_data[recent_key[0]]['2. high']) + float(price_data[recent_key[0]]['3. low'])) / 2
    return stock_price


def sel_stock(user, portfolios):
    # display portfolio
    print("your current portfolio is")
    display_portfolio(user, portfolios)

    print("From which company do you want to sell shares?")
    company = input("please enter the company ticker")
    print("\n")

    if company not in portfolios['users'][user]['portfolio']['stocks']:
        print("the company that you selected is not in your portfolio, please select another company")

        print("Do you want to continue?")
        choice = input("please enter [y/n]")
        print("\n")

        while choice == "y":
            sel_stock(user, portfolios)

        if choice == "n":
            print("you will return to the menu")
            print("\n")

    else:

        print("How many shares do you want to sell?")
        sell_quantity = float(input("please enter the amount of shares"))
        print("\n")

        if sell_quantity <= 0:
            print("The amount you entered is invalid, please enter a valid number of shares.")
            choice = input("Would you like to try again [y/n]")
            if choice == 'y':
                sel_stock(user, portfolios)
            else:
                print("back to menu")


            # vars to make code more readable
        current_quantity = portfolios['users'][user]['portfolio']['stocks'][company]['quantity']
        stock_price = 150  # current_stock_price(company)
        current_balance = portfolios['users'][user]['portfolio']['balance']

        if sell_quantity > current_quantity:
            print(
                f"You do not have that many shares in your possession, you currently have {current_quantity} shares of {company}")
            print("\n")

            print("Do you want to continue?")
            choice = input("please enter [y/n]")
            print("\n")

            while choice == "y":
                sel_stock(user, portfolios)
            if choice == "n":
                print("you will return to the menu")
                print("\n")


        if sell_quantity <= current_quantity:
            print(
                f"thank you, are you sure that you want to sell {sell_quantity} of {company} at the current price of {stock_price}?")
            choice = input("please confirm [y/n]")
            print("\n")

            if choice == "y":

                # update balance
                new_balance = current_balance + (stock_price * sell_quantity)
                current_balance += new_balance
                print(
                    f"transaction SELL of {sell_quantity} shares {company} with a total amount of {stock_price * sell_quantity} EURO completed")  # here the currency needs to be added
                print("\n")

                # update quantity
                portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] = (
                        portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] - sell_quantity)
                if portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] == 0:
                    del portfolios['users'][user]['portfolio']['stocks'][company]

                with open("Portfolios.json", 'w') as fp:
                    json.dump(portfolios, fp)

                # display portfolio
                print("your current portfolio after transaction is:")
                display_portfolio(user, portfolios)

            elif choice == "n":
                print("Do you want to continue?")
                choice = input("please enter [y/n]")
                print("\n")
                while choice == "y":
                    sel_stock(user, portfolios)
                if choice == "n":
                    print("you will return to the menu")
                    print("\n")





    return portfolios