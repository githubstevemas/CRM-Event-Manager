from config.config import global_db_session
from epic_events.controllers.validators import get_employee_id
from epic_events.models.client import Client
from epic_events.views.client_view import display_add_client, \
    display_ask_client_to_edit, display_client_field_to_edit
from epic_events.views.reports import display_clients


def get_clients(session=global_db_session):
    clients = session.query(Client).all()
    display_clients(clients)


def add_client(client_datas, commercial_id, db_session=global_db_session):

    try:
        new_client = Client(first_name=client_datas['first_name'],
                            last_name=client_datas['last_name'],
                            email=client_datas['email'],
                            phone=client_datas['phone'],
                            company_name=client_datas['company_name'],
                            commercial_id=commercial_id)

        db_session.add(new_client)
        db_session.commit()
        print("\nClient successfully added.")
        input("Type Enter to continue")

    except Exception as e:
        print(f"Error while adding client: {e}")


def get_client_datas_to_add():

    client_datas = display_add_client()
    commercial_id = get_employee_id()
    add_client(client_datas, commercial_id)


def edit_client():
    # get old client datas and ask user to edit

    client_to_edit = display_ask_client_to_edit()
    choice = display_client_field_to_edit(client_to_edit)

    try:
        if choice == 1:
            client_to_edit.first_name = input("Enter new first name: ")
        elif choice == 2:
            client_to_edit.last_name = input("Enter new last name: ")
        elif choice == 3:
            client_to_edit.email = input("Enter new email: ")
        elif choice == 4:
            client_to_edit.phone = input("Enter new phone: ")
        elif choice == 5:
            client_to_edit.company_name = input("Enter new company: ")
        else:
            print("Invalid choice.")

        global_db_session.commit()
        print("\nClient updated successfully.")
        input("Type Enter to continue")

    except Exception as e:
        global_db_session.rollback()
        print(f"An error occurred: {e}")
