from unittest.mock import patch

from epic_events.models.client import Client
from epic_events.models.employee import Employee
from epic_events.views.employee_view import get_department
from epic_events.views.reports import display_clients, display_employees


def test_get_department(capsys):
    with patch('builtins.input', return_value="1"):
        assert get_department() == "1"


def test_display_employees(db_session, insert_test_employee, capsys):
    # Insert new employee
    insert_test_employee(email="branda@exemple.com", password="password123",
                         first_name="Branda", last_name="Daniels",
                         phone="1234567890",
                         role_id=2)

    employees = db_session.query(Employee).all()

    display_employees(employees)
    captured = capsys.readouterr()

    assert "Branda" in captured.out


def test_display_clients(db_session, insert_test_client, capsys):

    # Insert new client
    insert_test_client(first_name="Brandon", last_name="Daniels",
                       email="brandon@exemple.com", phone="1234567890",
                       company_name="Coca-Cola", commercial_id=2)

    clients = db_session.query(Client).all()

    display_clients(clients)
    captured = capsys.readouterr()

    assert "Brandon" in captured.out
