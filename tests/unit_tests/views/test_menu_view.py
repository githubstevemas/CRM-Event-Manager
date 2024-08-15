from unittest.mock import patch

from epic_events.views.cli_menu import contract_menu, client_menu, \
    event_menu, employee_menu


def test_management_display(capsys):

    with patch('builtins.input', return_value='0'):
        contract_menu(role=1)
        captured = capsys.readouterr()
        assert "Add contract" in captured.out


def test_commercial_display(capsys):

    with patch('builtins.input', return_value='0'):
        client_menu(role=2)
        captured = capsys.readouterr()
        assert "Add client" in captured.out

    with patch('builtins.input', return_value='0'):
        contract_menu(role=2)
        captured = capsys.readouterr()
        assert "List not signed contracts" in captured.out


def test_support_display(capsys):

    with patch('builtins.input', return_value='0'):
        event_menu(role=3)
        captured = capsys.readouterr()
        assert "Edit event" in captured.out


def test_employee_menu():

    with patch('builtins.input', return_value='2'):
        assert employee_menu(role=1) == 2
