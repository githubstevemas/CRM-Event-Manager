from config.config import global_db_session
from epic_events.controllers.validators import get_client_datas

from epic_events.models import Contract
from epic_events.views.cli import display_add_contract
from epic_events.views.reports import display_contracts


def get_contracts():
    contracts = global_db_session.query(Contract).all()
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
    print("edit contract")
    pass
