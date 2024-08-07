import getpass

from config.config import global_db_session as session
from epic_events.controllers.validators import validate_email_adress, \
    validate_password
from epic_events.models.employee import Employee


def display_main_menu():
    # Display main menu

    print("\nMENU :\n\n"
          "[1] Client management\n"
          "[2] Contract management\n"
          "[3] Event management\n"
          "[4] Employee management\n"
          "[0] Exit")
    return input("You choice ? ")


def client_menu(role):

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

    while True:

        index = 1
        options = {}

        print("\nContract menu :\n\n")

        print(f"[{index}] List contracts")
        options[index] = "list_contracts"
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

    while True:

        index = 1
        options = {}

        print("\nEvent menu :\n\n")

        print(f"[{index}] List events")
        options[index] = "list_events"
        index += 1

        if role in [2]:
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


def get_department():
    # Get department user choice

    print("Select department number :\n")
    print("[1] Management")
    print("[2] Commercial")
    print("[3] Support")
    choice = input("\nYour choice ? ")
    if choice == '1':
        return "1"
    elif choice == '2':
        return "2"
    elif choice == '3':
        return "3"
    else:
        print("Invalid choice. Please try again.")
        return get_department()


def display_register():
    # Get employee datas

    first_name = input("First name ? ").lower()
    last_name = input("Last name ? ").lower()

    while True:
        password = input("Password ? (Min 8 characters, include uppercase & "
                         "lowercase, digits, symbols, and no spaces.) ")
        valid_password = validate_password(password)
        if valid_password:
            break
        else:
            print("Wrong password.")

    while True:
        email = input("Email ? ").lower()
        valid_email = validate_email_adress(email)

        if valid_email:
            existing_user = session.query(Employee).filter_by(email=email).first()
            if existing_user:
                print("Email already in db.")
            else:
                break
        else:
            print("Email adress not valid.")

    phone = input("Phone number ? ")
    role_id = get_department()

    new_employee = {'first_name': first_name,
                    'last_name': last_name,
                    'password': password,
                    'email': email,
                    'phone': phone,
                    'role_id': role_id}

    return new_employee


def display_employees(employees):
    print("Employees in db :")
    for employee in employees:
        print(f"ID: {employee.id}, "
              f"Name: {employee.first_name} {employee.last_name}, "
              f"Password: {employee.password}"
              f"Email: {employee.email}, "
              f"Department: {employee.role_id}")


def display_clients(clients):
    print("Clients in db :")
    for client in clients:
        print(f"ID: {client.id}, "
              f"Name: {client.first_name} {client.last_name}, "
              f"Email: {client.email}, "
              f"Company: {client.company_name}")


def ask_password():
    return getpass.getpass("Please enter your password : ")
