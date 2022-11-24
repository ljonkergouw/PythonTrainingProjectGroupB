class Portfolio:

    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0
        self.portfolio = {}
        self.portfolio_count = len(self.portfolio)

    def display_portfolio(self):
        print(f"Portfolio displayed for user {self.user_id}:")
        print(f'Your Portfolio contains {self.portfolio_count} stocks and your balance is €{self.balance}!')

    def add_money(self, amount):
        if type(amount) == float or type(amount) == int and amount > 0:
            self.balance += amount
            print(f'Your balance is now {self.balance}')
        else:
            print("The amount given is not a positive number!")

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("You are trying to withdraw more money than is currently in your balance!")
            print("Please provide an amount which is less or equal to your balance")

        elif type(amount) == float or type(amount) == int and amount > 0:
            print(f"{amount} is deducted from your balance which is {self.balance}")
            self.balance -= amount
            print(f'Your balance is now {self.balance}')
        else:
            print("The amount given is not a positive number!")


if __name__ == '__main__':
    Port1 = Portfolio('Louk123')
    Port1.display_portfolio()
    Port1.add_money(-150)
    Port1.add_money(10000)
    Port1.add_money(15000)

    Port1.withdraw_money(24499)
    Port1.withdraw_money(600)
