import requests
key = "EMFE4N5TBX48Y6W5"

def search(search_input):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={search_input}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    print(data)
    return data

def print_search_results(results):
    print(f"symbol\t name\t\t\t\t\t type\t region\t marketOpen\t marketClose\t timezone\t currency\t")
    print("-----------------------------------------------------------")
    for i in range(len(results['bestMatches'])):
        result = results['bestMatches'][i]
        print(f"{result['1. symbol']:<10} {result['2. name']:<60}{result['3. type']:<25}{result['4. region']:<20}{result['5. marketOpen']:<10}{result['6. marketClose']:<10}{result['7. timezone']:<20}{result['8. currency']:<20}")


if __name__ == "__main__":
    search_input = input("Please enter your search:")
    results = search(search_input)
    print(f"Your search resulted in a total of {len(results)} results")
    print_search_results(results)



