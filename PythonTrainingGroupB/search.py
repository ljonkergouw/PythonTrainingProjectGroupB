import requests
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
key = "EMFE4N5TBX48Y6W5"

def search(search_input):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={search_input}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    print(f"Your search resulted in a total of {len(data['bestMatches'])} results")
    return data

def print_search_results(results):
    print(f"symbol\t name\t\t\t\t\t type\t region\t marketOpen\t marketClose\t timezone\t currency\t")
    print("-----------------------------------------------------------")
    for i in range(len(results['bestMatches'])):
        result = results['bestMatches'][i]
        print(f"{result['1. symbol']:<10} {result['2. name']:<75}{result['3. type']:<25}{result['4. region']:<20}{result['5. marketOpen']:<10}{result['6. marketClose']:<10}{result['7. timezone']:<20}{result['8. currency']:<20}")


def stock_info(symbol, key):
    #url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={key}'
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={str(symbol).replace(".", "-")}&apikey={key}'

    r = requests.get(url)
    data = r.json()

    print('Info:')
    print(f"{'Symbol':<10} {'AssetType':<20} {'Name':<25}  {'Exchange':<10} {'Currency':<10} {'Country':<15} {'Industry':<50} {'DividendPerShare':<10}")
    print(f"{data['Symbol']:<10} {data['AssetType']:<20} {data['Name']:<25}  {data['Exchange']:<10} {data['Currency']:<10} {data['Country']:<15} {data['Industry']:<50} {data['DividendPerShare']:<10}")


def display_price_chart(symbol, key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval=15min&slice=year1month1&apikey={key}"

    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

        headers = my_list.pop(0)
        past_day = pd.DataFrame(my_list, columns=headers).head(96)
        x = past_day['time']
        x = np.asarray(x, dtype='datetime64[s]')
        sns.lineplot(data=past_day, x=x, y="high")


        plt.show()


if __name__ == "__main__":
    search_input = input("Please enter your search:")
    results = search(search_input)
    print_search_results(results)
    second_search = input("Of which of these stocks would you like to know more information? Please provide the ticker")
    stock_info(second_search, key)
    display_price_chart(second_search, key)



