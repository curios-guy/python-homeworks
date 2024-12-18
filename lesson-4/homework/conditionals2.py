while True:
    # ask user a password
    password = input("Please input password: ")

    # checks the length
    if len(password) < 8:
        print("Password is too short!")
    # checks the uppercase
    elif not password[0].isupper():
        print("First character must be uppercase!")
    # if all conditions are met, breaks
    else:
        print("Perfect!")
        break

