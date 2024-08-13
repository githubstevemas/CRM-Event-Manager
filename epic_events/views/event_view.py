from sqlalchemy.event import Events

from config.config import global_db_session
from epic_events.controllers.validators import get_contract_datas, \
    get_event_datas
from epic_events.views.reports import display_events


def display_add_event():
    while True:
        try:
            contract_id = int(input("Contract id? "))
            contract = get_contract_datas(contract_id)
            alright = input(
                f"Client {contract.client.first_name} "
                f"{contract.client.last_name} ? y/n: ")
            if alright.lower() == "y":
                break
        except ValueError:
            print("Invalid id.")
        except AttributeError:
            print("Contract not found.")

    start_date = input("Start date ? (YYYY-MM-DD HH:MM:SS) ")
    end_date = input("End date ? (YYYY-MM-DD HH:MM:SS) ")
    location = input("Location ? ")
    attendees = int(input("Attendees ? "))
    notes = input("Add notes : ")

    event_datas = {
        'contract_id': contract_id,
        'client_id': contract.client_id,
        'event_date_start': start_date,
        'event_date_end': end_date,
        'location': location,
        'attendees': attendees,
        'notes': notes
    }

    return event_datas


def display_ask_event_to_edit():
    while True:
        try:
            print("\nSelect event reference to edit. "
                  "Type 'list' to show all events")
            choice = input("Your choice ? ")

            if choice == "list":
                events_list = global_db_session.query(Events).all()
                display_events(events_list)
            else:
                try:
                    event = get_event_datas(choice)
                    alright = input(
                        f"Event for {event.client.first_name} "
                        f"{event.client.last_name} ? y/n: ")
                    if alright == "y":
                        break

                except ValueError:
                    print("Wrong answer.")

        except ValueError:
            print("Invalid id.")
        except AttributeError:
            print("Employee not found.")

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
