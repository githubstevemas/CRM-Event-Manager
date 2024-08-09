from config.config import global_db_session
from epic_events.controllers.validators import get_client_datas

from epic_events.models import Contract
from epic_events.views.cli import display_add_contract
from epic_events.views.reports import display_contracts


def get_contracts():
    contracts = global_db_session.query(Contract).all()
    display_contracts(contracts)


def add_contract():

    contract_datas = display_add_contract()

    client = get_client_datas(contract_datas['client_id'])

    new_contract = Contract(client_id=contract_datas['client_id'],
                            commercial_id=client.commercial_id,
                            amount=contract_datas['amount'],
                            left_to_pay=contract_datas['left_to_pay'])

    # Add new_contract to the db
    global_db_session.add(new_contract)
    global_db_session.commit()
    print("Contract successfully added.")


def edit_contract():
    print("edit contract")
    pass


def delete_contract():
    pass
