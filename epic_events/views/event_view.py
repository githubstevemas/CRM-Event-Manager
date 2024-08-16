from epic_events.controllers.contract_controller import \
    get_own_not_signed_contracts
from epic_events.controllers.employee_controller import get_support_employees
from epic_events.controllers.validators import get_contract_datas, \
    get_event_datas, is_numeric, validate_datetime, get_employee_datas, \
    get_employee_id


def display_add_event():

    employee_id = get_employee_id()
    contract = get_valid_contract(employee_id)
    start_date = get_valid_date("Start date")
    end_date = get_valid_date("End date")
    support_id = get_valid_support_id()
    location = input("Location? ")
    attendees = get_valid_attendees()
    notes = input("Add notes: ")

    event_datas = {
        'contract_id': contract.id,
        'client_id': contract.client_id,
        'event_date_start': start_date,
        'event_date_end': end_date,
        'support_id': support_id,
        'location': location,
        'attendees': attendees,
        'notes': notes
    }

    return event_datas


def get_valid_contract(employee_id):

    while True:
        get_own_not_signed_contracts()
        try:
            contract_id = int(input("Contract id? "))
            contract = get_contract_datas(contract_id)
            if contract.commercial_id == employee_id and not contract.status:
                alright = input(
                    f"Client {contract.client.first_name} "
                    f"{contract.client.last_name}? y/n: "
                )
                if alright.lower() == "y":
                    return contract
            else:
                print("Wrong contract Id.")
        except ValueError:
            print("Invalid id.")
        except AttributeError:
            print("Contract not found.")


def get_valid_date(prompt):

    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD HH:MM:SS): ")
        if validate_datetime(date_str):
            return date_str
        else:
            print("Format must be YYYY-MM-DD HH:MM:SS")


def get_valid_support_id():

    while True:
        get_support_employees()
        support_id = input("\nSupport employee Id? (type '0' to skip): ")
        if support_id == "0":
            return None
        elif is_numeric(support_id):
            try:
                employee = get_employee_datas(int(support_id))
                if employee.role_id == 3:
                    alright = input(
                        f"Employee support {employee.first_name} "
                        f"{employee.last_name}? y/n: "
                    )
                    if alright.lower() == "y":
                        return support_id
                    else:
                        print("Wrong answer.")
                else:
                    print("Wrong employee Id.")
            except ValueError:
                print("Wrong answer.")
            except AttributeError:
                print("Employee not found.")
        else:
            print("Wrong answer.")


def get_valid_attendees():

    while True:
        attendees = input("Attendees? ")
        if is_numeric(attendees):
            return int(attendees)
        else:
            print("Must be numeric.")


def display_ask_event_support_to_edit():

    while True:

        print("\nSelect event reference to edit.")
        choice = input("Your choice ? (type '0' to go back) ")
        if choice == "0":
            return None

        try:
            event = get_event_datas(int(choice))
            alright = input(
                f"Event for {event.client.first_name} "
                f"{event.client.last_name} ? y/n: ")
            if alright == "y":
                break

        except ValueError:
            print("Wrong answer.")

        except AttributeError:
            print("Event not found.")

    return event


def display_ask_event_to_edit(employee_id):

    while True:

        print("\nSelect event reference to edit.")
        choice = input("Your choice ? (type '0' to go back) ")
        if choice == "0":
            return None

        try:
            event = get_event_datas(int(choice))

            if event.support_id == employee_id:
                alright = input(
                    f"Event for {event.client.first_name} "
                    f"{event.client.last_name} ? y/n: ")
                if alright == "y":
                    break
            else:
                print("Wrong answer.")

        except ValueError:
            print("Wrong answer.")

        except AttributeError:
            print("Event not found.")

    return event


def display_event_field_to_edit(event_to_edit):

    print("\nCurrent information:")
    print(f"[1] Start date: {event_to_edit.event_start_date}")
    print(f"[2] End date: {event_to_edit.event_end_date}")
    print(f"[3] Location: {event_to_edit.location}")
    print(f"[4] Attendees: {event_to_edit.attendees}")
    print(f"[5] Notes: {event_to_edit.notes}")
    choice = int(input("\nWhich field to edit ? "))

    return choice
