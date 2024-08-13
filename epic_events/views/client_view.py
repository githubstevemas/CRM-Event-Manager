from config.config import global_db_session
from epic_events.controllers.validators import validate_email_adress, \
    get_client_datas
from epic_events.models import Client
from epic_events.views.reports import display_clients


def display_add_client():
    first_name = input("First name ? ").lower()
    last_name = input("Last name ? ").lower()
    while True:
        email = input("Email ? ").lower()
        valid_email = validate_email_adress(email)
        if valid_email:
            break
        else:
            print("Email adress not valid.")
    phone = input("Phone number ? ")
    company_name = input("Company name ? ").lower()

    client_datas = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'company_name': company_name
    }

    return client_datas


def display_ask_client_to_edit():

    while True:
        try:
            print("\nSelect client id to edit. "
                  "Type 'list' to show all clients")
            choice = input("Your choice ? ")

            if choice == "list":
                clients_list = global_db_session.query(Client).all()
                display_clients(clients_list)
            else:
                try:
                    client = get_client_datas(choice)
                    alright = input(
                        f"Employee {client.first_name} "
                        f"{client.last_name} ? y/n: ")
                    if alright == "y":
                        break

                except ValueError:
                    print("Wrong answer.")

        except ValueError:
            print("Invalid id.")
        except AttributeError:
            print("Employee not found.")

    return client


def display_client_field_to_edit(client_to_edit):

    print("\nCurrent information:")
    print(f"[1] First Name: {client_to_edit.first_name}")
    print(f"[2] Last Name: {client_to_edit.last_name}")
    print(f"[3] Email: {client_to_edit.email}")
    print(f"[4] Phone: {client_to_edit.phone}")
    print(f"[5] Company name: {client_to_edit.company_name}")
    choice = int(input("\nWhich field to edit ? "))

    return choice
