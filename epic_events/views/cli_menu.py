import getpass


def display_main_menu():
    # Main user menu, visible to all users

    print("\nMENU :\n\n"
          "[1] Client management\n"
          "[2] Contract management\n"
          "[3] Event management\n"
          "[4] Employee management\n"
          "[0] Exit")
    return input("You choice ? ")


def client_menu(role):
    # List clients to all users, add/edit only to commercials

    while True:

        print("\nClient menu :\n\n")
        print("[1] List clients")
        if role == 2:
            print("[2] Add client")
            print("[3] Edit client")
        print("[0] Return")

        choice = int(input("Your choice? "))

        if role == 2 and 0 <= choice < 4:
            return choice
        elif role != 2 and choice in [0, 1]:
            return choice
        else:
            print("Wrong choice. Please try again.")


def contract_menu(role):
    # List contracts to all users, add to managers, edit to managers/support

    while True:

        index = 1
        options = {}

        print("\nContract menu :\n\n")

        print(f"[{index}] List contracts")
        options[index] = "list_contracts"
        index += 1

        if role == 2:
            print(f"[{index}] List not signed contracts")
            options[index] = "list_not_signed_contracts"
            index += 1

            print(f"[{index}] List not payed contracts")
            options[index] = "list_not_payed_contracts"
            index += 1

        if role == 1:
            print(f"[{index}] Add contract")
            options[index] = "add_contract"
            index += 1

        if role in [1, 2]:
            print(f"[{index}] Edit contract")
            options[index] = "edit_contract"
            index += 1

        print("[0] Return")

        choice = int(input("Your choice? "))

        if 0 <= choice < index:
            return options.get(choice)
        else:
            print("Wrong choice. Please try again.")


def event_menu(role):
    # List events to all users, add to commercials, edit to support/management

    while True:

        index = 1
        options = {}

        print("\nEvent menu :\n\n")

        print(f"[{index}] List events")
        options[index] = "list_events"
        index += 1

        if role == 1:
            print(f"[{index}] List events with no support")
            options[index] = "list_no_support"
            index += 1

        if role == 3:
            print(f"[{index}] List own events")
            options[index] = "list_own_events"
            index += 1

        if role == 2:
            print(f"[{index}] Add event")
            options[index] = "add_event"
            index += 1

        if role in [1, 3]:
            print(f"[{index}] Edit event")
            options[index] = "edit_event"
            index += 1

        print("[0] Return")

        choice = int(input("Your choice? "))

        if 0 <= choice < index:
            return options.get(choice)
        else:
            print("Wrong choice. Please try again.")


def employee_menu(role):
    # List employees to all users, add/edit to managers

    while True:
        print("\nEmployee menu :\n\n")
        print("[1] List employees")
        if role == 1:
            print("[2] Add employee")
            print("[3] Edit employee")
        print("[0] Return")

        choice = int(input("Your choice? "))

        if role == 1 and 0 <= choice < 4:
            return choice
        elif role != 1 and choice in [0, 1]:
            return choice
        else:
            print("Wrong choice. Please try again.")


def ask_password():
    return getpass.getpass("Please enter your password : ")
