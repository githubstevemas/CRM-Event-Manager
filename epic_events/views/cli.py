import getpass


def display_main_menu():
    # Display main menu
    """
    créer un collaborateur ;
    modifier un collaborateur (y compris son département) ;
    créer un contrat ;
    modifier un contrat (tous les champs, y compris relationnels) ;
    créer un événement ;
    modifier un événement (tous les champs, y compris relationnels) ;
    """

    print("\nMENU :\n\n"
          "[1] Client management\n"
          "[2] Contract management\n"
          "[3] Event management\n"
          "[4] Employee management\n"
          "[0] Exit")
    return input("You choice ? ")


def client_menu():
    print("\nClient menu :\n\n"
          "[1] Add new client\n"
          "[2] Client employee\n"
          "[3] Display all clients\n"
          "[0] Return")
    return input("You choice ? ")


def contract_menu():
    print("\nContract menu :\n\n"
          "[1] Add new contract\n"
          "[2] Edit contract\n"
          "[3] Display all contracts\n"
          "[0] Return")
    return input("You choice ? ")


def event_menu():
    print("\nEvent menu :\n\n"
          "[1] Add new event\n"
          "[2] Edit event\n"
          "[3] Display all event\n"
          "[0] Return")
    return input("You choice ? ")


def employee_menu():
    print("\nEmployee menu :\n\n"
          "[1] Add new employee\n"
          "[2] Edit employee\n"
          "[3] Display all employees\n"
          "[0] Return")
    return input("You choice ? ")


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

    new_employee = {'first_name': input("First name ? ").lower(),
                    'last_name': input("Last name ? ").lower(),
                    'password': input("Password ? "),
                    'email': input("Email ? ").lower(),
                    'phone': input("Phone number ? "),
                    'role_id': get_department()}

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
