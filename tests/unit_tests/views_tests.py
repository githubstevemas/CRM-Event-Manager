from unittest.mock import patch

from epic_events.controllers.client_controller import get_clients
from epic_events.controllers.contract_controller import get_contracts
from epic_events.controllers.event_controller import get_events
from epic_events.controllers.validators import get_employee_datas, \
    get_client_datas, get_contract_datas
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


def test_get_employee_datas(db_session):

    employee = get_employee_datas(1, db_session)
    assert employee.first_name == 'john'


def test_get_client_datas(db_session):

    client = get_client_datas(1, db_session)
    assert client.first_name == 'jane'


def test_get_contract_datas(db_session):

    contract = get_contract_datas(1, db_session)
    assert contract.left_to_pay == 500


def test_get_contracts(db_session, capsys):

    get_contracts(db_session)
    captured = capsys.readouterr()

    assert "2000" in captured.out


def test_get_clients(db_session, capsys):

    get_clients(db_session)
    captured = capsys.readouterr()

    assert "jane" in captured.out


def test_get_events(db_session, capsys):

    get_events(db_session)
    captured = capsys.readouterr()

    assert "toulouse" in captured.out


def test_display_add_client():

    pass


def test_display_ask_client_to_edit():

    pass


def test_display_add_contract():
    # Saisie d'un id qui n'existe pas, assert display "Client not found."
    pass


def test_display_ask_contract_to_edit():

    pass


def test_display_add_event():
    # Saisie d'un id qui n'existe pas, assert display "Contract not found."
    pass


def test_display_ask_event_to_edit():

    pass


def test_display_add_employee():
    # Saisie d'un id qui n'existe pas, assert display "Employee not found."
    pass


def test_display_ask_employee_to_edit():

    pass
