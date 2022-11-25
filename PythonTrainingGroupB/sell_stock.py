def current_stock_price(company):
    response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&outputsize=full&apikey=AD3GLM6F3A21OGWC")
    raw_data = response.json()
    price_data = raw_data['Time Series (5min)']
    recent_key = list(price_data.keys())[:1]
    stock_price = (float(price_data[recent_key[0]]['2. high']) + float(price_data[recent_key[0]]['3. low'])) / 2
    return stock_price

def sel_stock():
    # display portfolio
    print("your current portfolio is")
    print("\n")
    print("---------------------------------------------")
    print("company \t quantity \t total amount")
    for key in portfolios['users'][user]['portfolio']['stocks']:
        print(
            f"{key} \t\t {portfolios['users'][user]['portfolio']['stocks'][key]['quantity']} \t\t {portfolios['users'][user]['portfolio']['stocks'][key]['quantity'] * current_stock_price(key)}")
    print("---------------------------------------------")
    print("\n")

    print("From which company do you want to sell shares?")
    company = input("please enter the company ticker")
    print("\n")

    if company not in portfolios['users'][user]['portfolio']['stocks']:
        print("the company that you selected is not in your portfolio, please select another company")
        sel_stock()

    else:

        print("How many shares do you want to sell?")
        sell_quantity = float(input("please enter the amount of shares"))
        print("\n")

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
                sel_stock()
            if choice == "n":
                print("you will return to the menu")
                print("\n")
                # koppeling maken naar menu

        if sell_quantity <= current_quantity:
            print(
                f"thank you, are you sure that you want to sell {sell_quantity} of {company} at the current price of {stock_price}?")
            choice = input("please confirm [y/n]")
            print("\n")

            if choice == "y":

                # update balance
                new_balance = current_balance + (stock_price * stock_quantity)
                current_balance += new_balance
                print(
                    f"transaction SELL of {sell_quantity} shares {company} with a total amount of {stock_price * sell_quantity} EURO completed")  # here the currency needs to be added
                print("\n")

                # update quantity
                portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] = (
                            portfolios['users'][user]['portfolio']['stocks'][company]['quantity'] - sell_quantity)

                # display portfolio
                print("your current portfolio is now")
                print("\n")

                print("---------------------------------------------")
                print("company \t quantity \t total amount")
                for key in portfolios['users'][user]['portfolio']['stocks']:
                    print(
                        f"{key} \t\t {portfolios['users'][user]['portfolio']['stocks'][key]['quantity']} \t\t {portfolios['users'][user]['portfolio']['stocks'][key]['quantity'] * 150}")  # * current_stock_price(company)}")
                print("---------------------------------------------")
                print("\n")

            elif choice == "n":
                print("Do you want to continue?")
                choice = input("please enter [y/n]")
                print("\n")
                while choice == "y":
                    sel_stock()
                if choice == "n":
                    print("you will return to the menu")
                    print("\n")
                    # koppeling maken naar menu
    return portfolios