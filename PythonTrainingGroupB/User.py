class UserName:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def welcome_message(self):
        print(f"Welcome {self.user_id}!\n\nThe user information of user_id {self.user_id}: No additional information")

    def create_portfolio(self):
        pass

if __name__ == '__main__':
    User1 = UserName('louk123', 'ABC123', 'Louk')
    User1.welcome_message()