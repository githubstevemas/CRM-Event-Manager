import datetime

import sentry_sdk

from config.config import global_db_session
from epic_events.controllers.validators import get_client_datas, \
    get_employee_id

from epic_events.models import Contract, Client
from epic_events.views.contract_view import display_add_contract, \
    display_ask_contract_to_edit, display_contract_field_to_edit
from epic_events.views.reports import display_contracts, display_clients


def get_contracts(session=global_db_session):

    contracts = session.query(Contract).all()
    display_contracts(contracts)
    input("Type Enter to continue")


def get_own_not_signed_contracts(session=global_db_session):
    # Get not signed contracts from curent user

    own_id = get_employee_id()
    own_signed_contracts = (session.query(Contract)
                            .filter(Contract.commercial_id == own_id)
                            .filter(Contract.status.is_(False))
                            .all())
    display_contracts(own_signed_contracts)


def get_not_signed_contracts(db_session=global_db_session):

    not_signed_contracts = (db_session.query(Contract)
                            .filter(Contract.status.is_(False)).all())
    display_contracts(not_signed_contracts)


def get_not_payed_contracts(db_session=global_db_session):

    not_payed_contracts = (db_session.query(Contract)
                           .filter(Contract.left_to_pay < Contract.amount)
                           .all())
    display_contracts(not_payed_contracts)


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
        print("\nContract successfully added.")
        input("Type Enter to continue")

    except Exception as e:
        print(f"\nError while adding contract: {e}")


def get_contract_datas_to_add(session=global_db_session):
    # Get datas from view function and get it to save in db

    clients_list = session.query(Client).all()
    display_clients(clients_list)
    contract_datas = display_add_contract()
    client_id = contract_datas['client_id']

    add_contract(contract_datas, client_id)


def edit_contract(session=global_db_session):
    # Get contract old contract datas and ask user to edit

    contracts_list = session.query(Contract).all()
    display_contracts(contracts_list)

    contract_to_edit = display_ask_contract_to_edit()
    if contract_to_edit is None:
        return

    choice = display_contract_field_to_edit(contract_to_edit)

    try:
        if choice == 1:
            contract_to_edit.amount = input("Enter new amount: ")
        elif choice == 2:
            contract_to_edit.left_to_pay = input("Enter new left to pay: ")
        elif choice == 3:
            contract_to_edit.status = int(input("Enter new status "
                                                "(type '1'for Signed) : "))
        else:
            print("Invalid choice.")

        contract_to_edit.contract_update_date = datetime.datetime.now()
        global_db_session.commit()
        print("\nContract updated successfully.")
        input("Type Enter to continue")

        if contract_to_edit.status == 1:
            sentry_sdk.capture_message(f"Contract id {contract_to_edit.id} "
                                       "successfully edited.")

    except Exception as e:
        global_db_session.rollback()
        print(f"An error occurred: {e}")
