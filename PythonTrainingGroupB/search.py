import requests
key = "EMFE4N5TBX48Y6W5"

def search(search_input):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={search_input}&apikey={key}'
    r = requests.get(url)
    data = r.json()
    print(data)

def print_search_results(results):
    print(f"symbol\t name\t typ\t region\t marketOpen\t market ")
    print("-----------------------------------------------------------")


if __name__ == "__main__":
    search_input = input("Please enter your search:")
    results = search(search_input)
    print(f"Your search resulted in a total of {len(results)} results")



