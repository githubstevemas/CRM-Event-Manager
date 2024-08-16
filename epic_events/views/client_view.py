from epic_events.controllers.validators import validate_email_adress, \
    get_client_datas


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


def display_ask_client_to_edit(employee_id):

    while True:

        print("\nSelect client id to edit.")
        choice = input("Your choice ? (type '0' to go back) ")
        if choice == "0":
            return None

        try:
            client = get_client_datas(int(choice))
            if client.commercial_id == employee_id:
                alright = input(
                    f"Client {client.first_name} "
                    f"{client.last_name} ? y/n: ")
                if alright == "y":
                    break
            else:
                print("Wrong answer.")

        except ValueError:
            print("Wrong answer.")

        except AttributeError:
            print("Client not found.")

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
