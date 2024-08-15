from unittest.mock import patch

from epic_events.controllers.employee_controller import get_employees


def test_get_employees(db_session, capsys):

    with patch('builtins.input', return_value='0'):
        get_employees(db_session)
        captured = capsys.readouterr()

        assert "john" in captured.out
