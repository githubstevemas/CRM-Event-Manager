from config.config import global_db_session
from epic_events.controllers.validators import get_employee_datas, \
    validate_email_adress, validate_password
from epic_events.models import Employee
from epic_events.views.reports import display_employees


def get_department():
    # Get department user choice

    while True:
        print("\nSelect department number :\n")
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
            print("Invalid choice.")


def display_add_employee():
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
            existing_user = global_db_session.query(Employee).filter_by(
                email=email).first()
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


def display_ask_employee_to_edit(session=global_db_session):

    while True:

        print("\nSelect employee id to edit. "
              "Type 'list' to show all employees")
        choice = input("Your choice ? ")

        if choice == "list":
            employees_list = session.query(Employee).all()
            display_employees(employees_list)
        else:
            try:
                employee = get_employee_datas(choice)
                alright = input(
                    f"Employee {employee.first_name} "
                    f"{employee.last_name} ? y/n: ")
                if alright == "y":
                    break

            except ValueError:
                print("Wrong answer.")

            except AttributeError:
                print("Employee not found.")

    return employee


def display_employee_field_to_edit(employee_to_edit):

    print("\nCurrent information:")
    print(f"[1] First Name: {employee_to_edit.first_name}")
    print(f"[2] Last Name: {employee_to_edit.last_name}")
    print(f"[3] Email: {employee_to_edit.email}")
    print(f"[4] Phone: {employee_to_edit.phone}")
    print(f"[5] Role ID: {employee_to_edit.role_id}")
    choice = int(input("\nWhich field to edit ? "))

    return choice
