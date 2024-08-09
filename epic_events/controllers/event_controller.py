from config.config import global_db_session
from epic_events.models import Event
from epic_events.views.reports import display_events


def get_events():

    events = global_db_session.query(Event).all()
    display_events(events)


def add_event():
    print("add event")
    pass


def edit_event():
    print("edit event")


def delete_event():
    pass
