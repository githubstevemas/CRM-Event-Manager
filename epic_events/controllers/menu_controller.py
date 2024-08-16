from epic_events.controllers.auth_controller import logout
from epic_events.controllers.client_controller import get_clients, \
    edit_client, get_client_datas_to_add
from epic_events.controllers.contract_controller import get_contracts, \
    edit_contract, get_contract_datas_to_add, get_not_signed_contracts, \
    get_not_payed_contracts
from epic_events.controllers.employee_controller import get_employees, \
    add_employee, edit_employee
from epic_events.controllers.event_controller import get_events, \
    edit_event, get_event_datas_to_add, get_event_no_support, get_own_events, \
    edit_event_support
from epic_events.controllers.permission_controller import verify_token, \
    verify_role
from epic_events.views.cli_menu import (display_main_menu,
                                        employee_menu,
                                        contract_menu,
                                        event_menu, client_menu)


def main_menu():

    while True:
        choice = display_main_menu()

        if choice == "666":

            result = 10 / 0
            print(result)

        if choice == "1":
            # Check permissions token to display client menu
            payload = verify_token()
            if payload:
                role_id = verify_role(payload)

                client_choice = client_menu(role_id)
                if client_choice == 1:
                    get_clients()
                elif client_choice == 2:
                    get_client_datas_to_add()
                elif client_choice == 3:
                    edit_client()

            else:
                # demander de se re-log
                pass

        if choice == "2":
            # Check permissions token to display contract menu

            payload = verify_token()
            if payload:
                role_id = verify_role(payload)
                contract_choice = contract_menu(role_id)
                if contract_choice == "list_contracts":
                    get_contracts()
                elif contract_choice == "list_not_signed_contracts":
                    get_not_signed_contracts()
                elif contract_choice == "list_not_payed_contracts":
                    get_not_payed_contracts()
                elif contract_choice == "add_contract":
                    get_contract_datas_to_add()
                elif contract_choice == "edit_contract":
                    edit_contract()
                elif contract_choice == "0":
                    main_menu()
            else:
                # demander de se re-log
                pass

        if choice == "3":
            # Check permissions token to display event menu

            payload = verify_token()
            if payload:
                role_id = verify_role(payload)
                event_choice = event_menu(role_id)
                if event_choice == "list_events":
                    get_events()
                elif event_choice == "list_no_support":
                    get_event_no_support()
                elif event_choice == "list_own_events":
                    get_own_events()
                elif event_choice == "add_event":
                    get_event_datas_to_add()
                elif event_choice == "edit_event":
                    edit_event()
                elif event_choice == "edit_event_support":
                    edit_event_support()
                elif event_choice == "0":
                    main_menu()
            else:
                # demander de se re-log
                pass

        if choice == "4":
            # Check permissions token to display employee menu

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
                elif employee_choice == 0:
                    main_menu()
            else:
                # demander de se re-log
                pass

        elif choice == "0":
            logout()
