from unittest.mock import patch
from epic_events.controllers.client_controller import add_client, get_clients
from epic_events.models import Client


def test_add_client(db_session, test_engine):

    new_client = {
        'first_name': 'jane',
        'last_name': 'doe',
        'email': 'j.doe@mail.com',
        'phone': '123456789',
        'company_name': 'coca-cola'
    }

    commercial_id = 1

    with patch('builtins.input', return_value=''):
        add_client(new_client, commercial_id, db_session)

        assert db_session.query(Client).filter_by(
            email='j.doe@mail.com').first() is not None


def test_get_clients(db_session, capsys):

    with patch('builtins.input', return_value='0'):
        get_clients(db_session)
        captured = capsys.readouterr()

        assert "jane" in captured.out
