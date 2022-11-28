from Portfolio import display_portfolio
import pandas as pd
import json
from currency.py import get_currency

def buy_current_stock_price(company):
    from dateutil import parser

    dt = datetime.now()
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
    stock_price = float(price_data[recent_key[0]]['2. high'])

    return stock_price

def buy_stock(user, portfolios):

    display_portfolio(user, portfolios)

    print("From which company do you want to buy shares?")
    company = input("please enter the company ticker")
    print("\n")

    buy_quantity = float(input("how many shares do you want to purchase?"))
    print("\n")

    if buy_quantity <= 0:
        print("The amount you entered is invalid, please enter a valid number of shares.")
        choice = input("Would you like to try again [y/n]")
        if choice == 'y':
            buy_stock(user, portfolios)
        else:
            print("back to menu")

    stock_price = float(buy_current_stock_price(company), 2)
    current_balance = portfolios['users'][user]['portfolio']['balance']
    currency = get_currency(company, "EMFE4N5TBX48Y6W5")

    if currency == 'EUR':
        stock_price = stock_price / 1.04
    else:

        if current_balance - (stock_price * buy_quantity) < 0:
            print(
                f"your funds are insufficient. In order to complete this transaction, please increase your balance by {abs(current_balance - (stock_price * buy_quantity))}")
            choice = input("do you want to make a deposit [y/n]?")
            if choice == 'y':
                print("go to make a deposit")
            if choice == 'n':
                print("go to menu")
        else:
            print(
                f"Are you sure you want to buy {buy_quantity} of {company} for a total amount of {buy_quantity * stock_price}?")
            choice = input("Please enter [y/n]")
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
                print("transaction completed")
                print("---------------------------------------------")
                print(f"shares bought: {buy_quantity}")
                print(f"company: {company}")
                print(f"total amount: {stock_price * buy_quantity}")
                print(f"currency: EURO")  # here the currency needs to be added
                print("\n")

                # current portfolio
                print("Portfolio after transaction:")
                display_portfolio(user, portfolios)

                choice = input("Do you want to continue [y/n]?")
                if choice == 'y':
                    buy_stock(user, portfolios)
                else:
                    print("back to menu")
                    print("\n")


    return portfolios