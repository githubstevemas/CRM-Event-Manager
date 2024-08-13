from unittest.mock import patch

from sqlalchemy import inspect

from epic_events.controllers.auth_controller import (is_email_exists,
                                                     hash_password,
                                                     verify_password,
                                                     register_employee)
from epic_events.controllers.client_controller import add_client
from epic_events.controllers.contract_controller import add_contract
from epic_events.controllers.event_controller import add_event
from epic_events.controllers.permission_controller import verify_token
from epic_events.controllers.validators import validate_password, \
    validate_email_adress, get_employee_datas, get_client_datas, \
    get_contract_datas
from epic_events.models import Client, Contract, Event
from epic_events.models.employee import Employee
from epic_events.views.cli_menu import client_menu, contract_menu, event_menu
from tests.conftest import insert_roles_in_table


def test_db_connection(test_engine):
    inspector = inspect(test_engine)

    assert inspector.engine.url.database == "test_epic_events"


def test_register_employee(db_session, test_engine):
    insert_roles_in_table(db_session)

    password_test = "qwertyui"

    hashed_password = hash_password(password_test)

    test_employee = {'first_name': "john",
                     'last_name': "doe",
                     'password': hashed_password,
                     'email': 'test@epic-events.com',
                     'phone': '+33531313131',
                     'role_id': 2}

    register_employee(test_employee, db_session)

    assert db_session.query(Employee).filter_by(
        email='test@epic-events.com').first() is not None


def test_hash_password():
    password_test = "qwertyui"
    hashed_password = hash_password(password_test)

    assert password_test != hashed_password


def test_is_email_exists(db_session, insert_test_employee):
    email_test = "jack@exemple.com"

    # Insert new employee
    insert_test_employee(email=email_test, password="password123",
                         first_name="Jack", last_name="Smith",
                         phone="1234567890",
                         role_id=2)

    assert is_email_exists(email_test, db_session)


def test_verify_password(db_session, insert_test_employee):
    password = "password123"
    email_test = "nicole@exemple.com"

    # Insert new employee
    insert_test_employee(email=email_test, password=password,
                         first_name="Nicole", last_name="Ryann",
                         phone="1234567890",
                         role_id=2)

    assert verify_password(password, email_test, db_session)


def test_verify_token(capsys):
    result = verify_token('tokens/test_token.txt')
    captured = capsys.readouterr()

    assert result is False
    assert "Wrong token." in captured.out


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


def test_support_display(capsys):
    with patch('builtins.input', return_value='0'):
        event_menu(role=3)
        captured = capsys.readouterr()
        assert "Edit event" in captured.out


def test_add_client(db_session, test_engine):

    new_client = {
        'first_name': 'jane',
        'last_name': 'doe',
        'email': 'j.doe@mail.com',
        'phone': '123456789',
        'company_name': 'coca-cola'
    }

    commercial_id = 1

    add_client(new_client, commercial_id, db_session)

    assert db_session.query(Client).filter_by(
        email='j.doe@mail.com').first() is not None


def test_add_contract(db_session, test_engine):

    new_contract = {
        'amount': '2000',
        'left_to_pay': '500',
    }

    client_id = 1

    add_contract(new_contract, client_id, db_session)

    assert db_session.query(Contract).filter_by(
        amount='2000').first() is not None


def test_add_event(db_session, test_engine):

    new_event = {
        'contract_id': '1',
        'client_id': '1',
        'left_to_pay': '500',
        'event_date_start': '2024/12/18 15:25:00',
        'event_date_end': '2024/12/19 15:25:00',
        'location': 'toulouse',
        'attendees': '200',
        'notes': 'bring k-way',
    }

    support_id = 1
    add_event(new_event, support_id, db_session)

    assert db_session.query(Event).filter_by(
        location='toulouse').first() is not None


def test_validate_password():
    wrong_password = "wrong"
    assert not validate_password(wrong_password)

    good_password = "Good@p4ssword"
    assert validate_password(good_password)


def test_validate_email():
    wrong_email = "wrong.email"
    assert not validate_email_adress(wrong_email)

    good_email = "good@email.com"
    assert validate_email_adress(good_email)


def test_get_employee_datas(db_session):

    employee = get_employee_datas(1, db_session)
    assert employee.first_name == 'john'


def test_get_client_datas(db_session):

    client = get_client_datas(1, db_session)
    assert client.first_name == 'jane'


def test_get_contract_datas(db_session):

    contract = get_contract_datas(1, db_session)
    assert contract.left_to_pay == 500
