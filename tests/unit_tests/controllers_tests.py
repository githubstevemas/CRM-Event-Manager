from unittest.mock import patch

from sqlalchemy import inspect

from epic_events.controllers.auth_controller import (is_email_exists,
                                                     hash_password,
                                                     verify_password,
                                                     register_employee)
from epic_events.controllers.permission_controller import verify_token
from epic_events.controllers.validators import validate_password, \
    validate_email_adress
from epic_events.models.employee import Employee
from epic_events.views.cli import client_menu, contract_menu, event_menu
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
                     'role_id': 1}

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
