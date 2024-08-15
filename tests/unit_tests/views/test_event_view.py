from unittest.mock import patch

from epic_events.views.event_view import get_valid_date


def test_get_valid_date(db_session, capsys):

    with patch('builtins.input', return_value='2185-11-21 15:30:00'):
        assert get_valid_date('enter date')
