print("Welcome to our Investment Game! If you want to sign up, press '0'. If you already have an account, press '1' to log in.")

choice = int(input("Please make your choice: "))

usernames_passwords = {'Luuk': 'Jonko'}

if choice == 0:
    new_username = input("Please enter a username: ")
    while (new_username in usernames_passwords):
        print("User name already exists, please enter another username: ")
        new_username = input("Please enter a username: ")
    new_password = input("Please enter a password: ")

    print("Thank you. In order to complete your registration, we need some additional details. Please enter your first name")
    first_name = input("First name: ")
    print("Registration completed")

    usernames_passwords[new_username] = new_password
    # print(usernames_passwords)



elif choice == 1:
    print("Please enter you username.")

    while True:
        existing_username = input("Username: ")
        if existing_username in usernames_passwords:
            existing_password = input("Please enter your password: ")
            if usernames_passwords[existing_username] == existing_password:
                print("Log in succesful")
                break
            else:
                print("You entered the wrong username/password combination. Please try again.")
        else:
            print("You didn't enter an existing username. Please try again ")







