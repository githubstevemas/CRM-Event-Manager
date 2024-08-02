import getpass


def display_main_menu():
    # Display main menu

    print("\nMENU :\n\n[1] Register employee\n[2] Display employees\n"
          "[3] Display clients")
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

    new_employee = [
        input("First name ? ").lower(),
        input("Last name ? ").lower(),
        input("Password ? "),
        input("Email ? ").lower(),
        input("Phone number ? "),
        get_department()
    ]

    return new_employee


def display_employees(employees):

    print("Employees in db :")
    for employee in employees:
        print(f"ID: {employee.id}, "
              f"Name: {employee.first_name} {employee.last_name}, "
              f"Email: {employee.email}, "
              f"Department: {employee.role_id.value}")


def display_clients(clients):

    print("Clients in db :")
    for client in clients:
        print(f"ID: {client.id}, "
              f"Name: {client.first_name} {client.last_name}, "
              f"Email: {client.email}, "
              f"Company: {client.company_name}")


def ask_password():
    return getpass.getpass("Please enter your password : ")
