from unittest.mock import patch

from epic_events.models import Client
from epic_events.views.client_view import display_add_client
from epic_events.views.reports import display_clients


def test_display_clients(db_session, insert_test_client, capsys):

    insert_test_client(first_name="Brandon", last_name="Daniels",
                       email="brandon@exemple.com", phone="1234567890",
                       company_name="Coca-Cola", commercial_id=2)

    clients = db_session.query(Client).all()

    display_clients(clients)
    captured = capsys.readouterr()

    assert "Brandon" in captured.out


def test_display_add_client(db_session, capsys):

    with patch('builtins.input', side_effect=['mathiew',
                                              'scott',
                                              'mathiew@exemple.com',
                                              '123456789',
                                              'Test Company']):

        new_test_client = display_add_client()

        assert new_test_client['first_name'] == 'mathiew'
