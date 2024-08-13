import sentry_sdk
from argon2 import PasswordHasher

from config.config import global_db_session
from epic_events.controllers.auth_controller import register_employee
from epic_events.models.employee import Employee
from epic_events.views.employee_view import display_ask_employee_to_edit, \
    get_department, display_add_employee, display_employee_field_to_edit

from epic_events.views.reports import display_employees

ph = PasswordHasher()


def get_employees():
    employees = global_db_session.query(Employee).all()
    display_employees(employees)


def add_employee():
    new_employee = display_add_employee()
    register_employee(new_employee)

    sentry_sdk.capture_message(f"Employee {new_employee['first_name']}"
                               f" {new_employee['last_name_name']}"
                               "successfully added.")

    print("Employee successfully added.")


def edit_employee():
    # Get old employee datas and ask user to edit

    employee_to_edit = display_ask_employee_to_edit()
    choice = display_employee_field_to_edit(employee_to_edit)

    try:
        if choice == 1:
            employee_to_edit.first_name = input("Enter new first name: ")
        elif choice == 2:
            employee_to_edit.last_name = input("Enter new last name: ")
        elif choice == 3:
            employee_to_edit.email = input("Enter new email: ")
        elif choice == 4:
            employee_to_edit.phone = input("Enter new phone: ")
        elif choice == 5:
            employee_to_edit.role_id = get_department()
        else:
            print("Invalid choice.")

        global_db_session.commit()
        print("Employee updated successfully.")
        sentry_sdk.capture_message(f"Employee {employee_to_edit.first_name}"
                                   " {employee_to_edit.last_name_name}"
                                   "successfully edited.")

    except Exception as e:
        global_db_session.rollback()
        print(f"An error occurred: {e}")
