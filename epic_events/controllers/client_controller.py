from config.config import SessionFactory
from epic_events.models.client import Client
from epic_events.views.cli import display_clients


def get_clients():

    clients = SessionFactory.query(Client).all()
    display_clients(clients)
