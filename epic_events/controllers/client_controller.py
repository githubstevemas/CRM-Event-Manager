from config.config import global_db_session
from epic_events.controllers.validators import get_employee_id
from epic_events.models.client import Client
from epic_events.views.cli import display_add_client
from epic_events.views.reports import display_clients


def get_clients():
    clients = global_db_session.query(Client).all()
    display_clients(clients)


def add_client():

    client_datas = display_add_client()
    commercial_id = get_employee_id()

    new_client = Client(first_name=client_datas['first_name'],
                        last_name=client_datas['last_name'],
                        email=client_datas['email'],
                        phone=client_datas['phone'],
                        company_name=client_datas['company_name'],
                        commercial_id=commercial_id)

    # Add new_client to the db
    global_db_session.add(new_client)
    global_db_session.commit()
    print("Client successfully added.")


def edit_client():
    print("edit client")
    pass


def delete_client():
    pass
