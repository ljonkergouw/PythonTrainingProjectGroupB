class User:

    def __init__(self, user_id, password, first_name):
        self.user_id = user_id
        self.password = password
        self.first_name = first_name

    def welcome_message(self):
        print(f"Welcome {self.first_name}!\n\nThe user information of user_id {self.user_id}: \n FirstName:{self.first_name}")

    def create_portfolio(self):
        pass


if __name__ == '__main__':
    User1 = User('louk123', 'ABC123', 'Louk')
    User1.welcome_message()