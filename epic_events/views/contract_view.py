from config.config import global_db_session
from epic_events.controllers.validators import get_client_datas, \
    get_contract_datas, is_numeric
from epic_events.models import Contract
from epic_events.views.reports import display_contracts


def display_add_contract():
    while True:
        try:
            client_id = int(input("Client id? "))
            client = get_client_datas(client_id)
            alright = input(
                f"Client {client.first_name} {client.last_name} ? y/n: ")
            if alright.lower() == "y":
                break
        except ValueError:
            print("Invalid id.")
        except AttributeError:
            print("Client not found.")

    while True:
        amount = int(input("Event amount in $ ? "))
        if is_numeric(amount):
            break
        else:
            print("Must be numeric.")

    while True:
        already_payed = int(input("Already payed in $ ? "))
        if is_numeric(already_payed):
            break
        else:
            print("Must be numeric.")

    left_to_pay = amount - already_payed

    contract_datas = {
        'client_id': client_id,
        'amount': amount,
        'left_to_pay': left_to_pay
    }

    return contract_datas


def display_ask_contract_to_edit():

    while True:
        try:
            print("\nSelect contract reference to edit. "
                  "Type 'list' to show all contracts")
            choice = input("Your choice ? ")

            if choice == "list":
                contracts_list = global_db_session.query(Contract).all()
                display_contracts(contracts_list)
            else:
                try:
                    contract = get_contract_datas(choice)
                    alright = input(
                        f"Contract {contract.client.first_name} "
                        f"{contract.client.last_name} ? y/n: ")
                    if alright == "y":
                        break

                except ValueError:
                    print("Wrong answer.")

        except ValueError:
            print("Invalid id.")
        except AttributeError:
            print("Employee not found.")

    return contract


def display_contract_field_to_edit(contract_to_edit):

    print("\nCurrent information:")
    print(f"[1] Amount: {contract_to_edit.amount}")
    print(f"[2] Left to pay: {contract_to_edit.left_to_pay}")
    print(f"[3] Status: {contract_to_edit.status}")
    choice = int(input("\nWhich field to edit ? "))

    return choice
