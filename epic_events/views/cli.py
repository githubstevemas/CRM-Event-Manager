from config import session
from epic_events.controllers.authentication import register
from epic_events.models.employee import Employee


def main_menu():
    # Display main menu

    print("\nMENU :\n\n[1] Register employee\n[2] Display employees\n")
    choice = input("You choice ? ")
    if choice == "1":
        register_employee()
    else:
        display_employees()


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


def register_employee():
    # Get employee datas

    first_name = input("First name ? ").lower()
    last_name = input("Last name ? ").lower()
    password = input("Password ? ")
    email = input("Email ? ").lower()
    phone = input("Phone number ? ")
    role_id = get_department()

    register(first_name,
             last_name,
             password,
             email,
             phone,
             role_id,
             session)


def display_employees():
    employees = session.query(Employee).all()

    for employee in employees:
        print(f"ID: {employee.id}, "
              f"Name: {employee.first_name} {employee.last_name}, "
              f"Email: {employee.email}, "
              f"Department: {employee.role_id.value}")


main_menu()
