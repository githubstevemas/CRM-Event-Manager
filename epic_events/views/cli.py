from config import session
from epic_events.models.employee import Employee


def main_menu():
    # Display main menu

    print("\nMENU :\n\n[1] Register employee\n[2] Display employees\n")
    choice = input("You choice ? ")
    if choice == "1":
        register_employee()
    else:
        display_employees()


def register_employee():
    # Get employee datas

    new_employee = Employee(
        first_name=input("First name ? "),
        last_name=input("Last name ? "),
        password=input("Password ? "),
        email=input("Email ? "),
        phone=input("Phone number ? "),
        department=input("Department ? ")
    )

    session.add(new_employee)
    session.commit()


def display_employees():

    employees = session.query(Employee).all()

    for employee in employees:
        print(f"ID: {employee.id}, Name: {employee.first_name} {employee.last_name}, Email: {employee.email}, Department: {employee.department}")


main_menu()
