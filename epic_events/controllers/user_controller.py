from epic_events.controllers.auth_controller import logout
from epic_events.controllers.client_controller import get_clients
from epic_events.controllers.employee_controller import register_employee, \
    get_employees
from epic_events.views.cli import (display_main_menu,
                                   employee_menu,
                                   contract_menu,
                                   event_menu, client_menu)


def main_menu():

    choice = display_main_menu()
    if choice == "1":
        client_choice = client_menu()
        if client_choice == "1":
            pass
        if client_choice == "2":
            pass
        if client_choice == "3":
            get_clients()
        elif client_choice == "0":
            main_menu()

    elif choice == "2":
        contract_choice = contract_menu()
        if contract_choice == "1":
            pass
        if contract_choice == "2":
            pass
        if contract_choice == "3":
            pass
        elif contract_choice == "0":
            main_menu()

    elif choice == "3":
        event_choice = event_menu()
        if event_choice == "1":
            pass
        if event_choice == "2":
            pass
        if event_choice == "3":
            pass
        elif event_choice == "0":
            main_menu()

    if choice == "4":
        employee_choice = employee_menu()
        if employee_choice == "1":
            register_employee()
        if employee_choice == "2":
            pass
        if employee_choice == "3":
            get_employees()
        elif employee_choice == "0":
            main_menu()

    elif choice == "0":
        logout()
