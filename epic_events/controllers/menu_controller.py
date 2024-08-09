from epic_events.controllers.auth_controller import logout
from epic_events.controllers.client_controller import get_clients, \
    add_client, edit_client, delete_client
from epic_events.controllers.contract_controller import get_contracts, \
    add_contract, edit_contract, delete_contract
from epic_events.controllers.employee_controller import get_employees, \
    add_employee, edit_employee, delete_employee
from epic_events.controllers.event_controller import get_events, add_event, \
    edit_event, delete_event
from epic_events.controllers.permission_controller import verify_token, \
    verify_role
from epic_events.controllers.validators import get_employee_id
from epic_events.views.cli import (display_main_menu,
                                   employee_menu,
                                   contract_menu,
                                   event_menu, client_menu)


def main_menu():

    while True:
        choice = display_main_menu()

        if choice == "999":

            add_employee()

        if choice == "666":

            id = get_employee_id()
            print(f"id de l'employee {id}")

        if choice == "1":
            payload = verify_token()
            if payload:
                role_id = verify_role(payload)

                client_choice = client_menu(role_id)
                if client_choice == 1:
                    get_clients()
                elif client_choice == 2:
                    add_client()
                elif client_choice == 3:
                    edit_client()
                elif client_choice == 4:
                    delete_client()

            else:
                # demander de se re-log
                pass

        if choice == "2":
            payload = verify_token()
            if payload:
                role_id = verify_role(payload)
                contract_choice = contract_menu(role_id)
                if contract_choice == "list_contracts":
                    get_contracts()
                elif contract_choice == "add_contract":
                    add_contract()
                elif contract_choice == "edit_contract":
                    edit_contract()
                elif contract_choice == "delete_contract":
                    delete_contract()
                elif contract_choice == "0":
                    main_menu()
            else:
                # demander de se re-log
                pass

        if choice == "3":
            payload = verify_token()
            if payload:
                role_id = verify_role(payload)
                event_choice = event_menu(role_id)
                if event_choice == "list_events":
                    get_events()
                elif event_choice == "add_event":
                    add_event()
                elif event_choice == "edit_event":
                    edit_event()
                elif event_choice == "delte_event":
                    delete_event()
                elif event_choice == "0":
                    main_menu()
            else:
                # demander de se re-log
                pass

        if choice == "4":
            payload = verify_token()
            if payload:
                role_id = verify_role(payload)
                employee_choice = employee_menu(role_id)
                if employee_choice == 1:
                    get_employees()
                elif employee_choice == 2:
                    add_employee()
                elif employee_choice == 3:
                    edit_employee()
                elif employee_choice == 4:
                    delete_employee()
                elif employee_choice == 0:
                    main_menu()
            else:
                # demander de se re-log
                pass

        elif choice == "0":
            logout()
