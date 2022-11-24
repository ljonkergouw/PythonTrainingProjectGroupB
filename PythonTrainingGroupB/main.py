print("Welcome to our Investment Game! If you want to sign up, press '0'. If you already have an account, press '1' to log in.")
choice = int(input("Please make your choice: "))

usernames_passwords = {}

if choice == 0:
    new_username = input("Please enter a user name: ")
    while new_username in usernames_passwords:
        print("User name already exists, please enter another user name: ")
        new_username = input("Please enter a user name: ")
    new_password = input("Please enter a passwords: ")

    print("Thank you. In order to complete your registration, we need some personal details. Please enter your first name")
    first_name = input("First name: ")

    usernames_passwords[new_username] = new_password
    print(usernames_passwords)

elif choice == 1:
    input("Please enter you username and password: ")
    existing_username = input("User name: ")
    existing_password = input("Password: ")
    if existing_username in usernames_passwords:







