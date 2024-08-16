from config.config import global_db_session
from epic_events.controllers.validators import get_employee_id
from epic_events.models import Event
from epic_events.views.event_view import display_add_event, \
    display_ask_event_to_edit, display_event_field_to_edit, \
    display_ask_event_support_to_edit, get_valid_support_id
from epic_events.views.reports import display_events


def get_events(session=global_db_session):

    events = session.query(Event).all()
    display_events(events)
    input("Type Enter to continue")


def get_event_no_support(session=global_db_session):

    events_no_support = (session.query(Event)
                         .filter(Event.support_id is None).all())
    display_events(events_no_support)
    input("Type Enter to continue")


def get_own_events(session=global_db_session):

    own_id = get_employee_id()
    own_events = (session.query(Event)
                         .filter(Event.support_id == own_id).all())
    display_events(own_events)


def add_event(event_datas, db_session=global_db_session):

    new_event = Event(contract_id=event_datas['contract_id'],
                      client_id=event_datas['client_id'],
                      event_date_start=event_datas['event_date_start'],
                      event_date_end=event_datas['event_date_end'],
                      support_id=event_datas['support_id'],
                      location=event_datas['location'],
                      attendees=event_datas['attendees'],
                      notes=event_datas['notes'])

    # Add new_event to the db
    db_session.add(new_event)
    db_session.commit()
    print("\nEvent successfully added.")
    input("Type Enter to continue")


def get_event_datas_to_add():
    # Get datas from view function and save it in db

    event_datas = display_add_event()
    add_event(event_datas)


def edit_event_support():

    get_events()
    event_to_edit = display_ask_event_support_to_edit()

    if event_to_edit is None:
        return

    employee_id = get_valid_support_id()

    try:
        event_to_edit.support_id = employee_id
        global_db_session.commit()
        print("\nEvent updated successfully.")
        input("Type Enter to continue")

    except Exception as e:
        global_db_session.rollback()
        print(f"An error occurred: {e}")


def edit_event():
    # Get old event datas and ask user to edit

    employee_id = get_employee_id()
    get_own_events()
    event_to_edit = display_ask_event_to_edit(employee_id)

    if event_to_edit is None:
        return

    choice = display_event_field_to_edit(event_to_edit)

    try:
        if choice == 1:
            event_to_edit.event_stat_date = input("Enter new start date: ")
        elif choice == 2:
            event_to_edit.event_end_date = input("Enter new end date: ")
        elif choice == 3:
            event_to_edit.location = input("Enter new location: ")
        elif choice == 4:
            event_to_edit.attendees = input("Enter new attendees number: ")
        elif choice == 5:
            event_to_edit.notes = input("Enter new notes: ")
        else:
            print("Invalid choice.")

        global_db_session.commit()
        print("\nEvent updated successfully.")
        input("Type Enter to continue")

    except Exception as e:
        global_db_session.rollback()
        print(f"An error occurred: {e}")
