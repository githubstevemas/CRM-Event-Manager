from unittest.mock import patch
from epic_events.controllers.event_controller import add_event, get_events
from epic_events.models import Event


def test_add_event(db_session, test_engine):

    new_event = {
        'contract_id': '1',
        'client_id': '1',
        'left_to_pay': '500',
        'event_date_start': '2024/12/18 15:25:00',
        'event_date_end': '2024/12/19 15:25:00',
        'support_id': '1',
        'location': 'toulouse',
        'attendees': '200',
        'notes': 'bring k-way',
    }

    with patch('builtins.input', return_value='0'):
        add_event(new_event, db_session)

        assert db_session.query(Event).filter_by(
            location='toulouse').first() is not None


def test_get_events(db_session, capsys):

    with patch('builtins.input', return_value='0'):
        get_events(db_session)
        captured = capsys.readouterr()

        assert "toulouse" in captured.out
