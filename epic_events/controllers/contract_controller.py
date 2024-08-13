import sentry_sdk

from config.config import global_db_session
from epic_events.controllers.validators import get_client_datas

from epic_events.models import Contract
from epic_events.views.contract_view import display_add_contract, \
    display_ask_contract_to_edit, display_contract_field_to_edit
from epic_events.views.reports import display_contracts


def get_contracts(db_session=global_db_session):
    contracts = db_session.query(Contract).all()
    display_contracts(contracts)


def add_contract(contract_datas, client_id, db_session=global_db_session):
    client = get_client_datas(client_id)

    try:
        new_contract = Contract(client_id=client_id,
                                commercial_id=client.commercial_id,
                                amount=contract_datas['amount'],
                                left_to_pay=contract_datas['left_to_pay'])

        # Add new_contract to the db
        db_session.add(new_contract)
        db_session.commit()
        print("Contract successfully added.")

    except Exception as e:
        print(f"Error while adding contract: {e}")


def get_contract_datas_to_add():
    contract_datas = display_add_contract()
    client_id = contract_datas['client_id']

    add_contract(contract_datas, client_id)


def edit_contract():
    # Get contract old contract datas and ask user to edit

    contract_to_edit = display_ask_contract_to_edit()
    choice = display_contract_field_to_edit(contract_to_edit)

    try:
        if choice == 1:
            contract_to_edit.amount = input("Enter new amount: ")
        elif choice == 2:
            contract_to_edit.left_to_pay = input("Enter new left to pay: ")
        elif choice == 3:
            contract_to_edit.status = input("Enter new status: ")
        else:
            print("Invalid choice.")

        global_db_session.commit()
        print("Contract updated successfully.")

        if contract_to_edit.status == 1:
            sentry_sdk.capture_message(f"Contract id {contract_to_edit.id} "
                                       "successfully edited.")

    except Exception as e:
        global_db_session.rollback()
        print(f"An error occurred: {e}")
