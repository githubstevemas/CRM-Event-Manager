from sqlalchemy import inspect

from epic_events.controllers.auth_controller import (is_email_exists,
                                                     hash_password,
                                                     verify_password,
                                                     register_employee,
                                                     create_encrypted_token,
                                                     save_token)
from epic_events.controllers.permission_controller import verify_token, \
    load_token
from epic_events.models.employee import Employee
from tests.conftest import insert_roles_in_table

TEST_TOKEN_PATH = 'tokens/test_token.txt'


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

    insert_test_employee(email=email_test, password="password123",
                         first_name="Jack", last_name="Smith",
                         phone="1234567890",
                         role_id=2)

    assert is_email_exists(email_test, db_session)


def test_verify_password(db_session, insert_test_employee):

    password = "password123"
    email_test = "nicole@exemple.com"

    insert_test_employee(email=email_test, password=password,
                         first_name="Nicole", last_name="Ryann",
                         phone="1234567890",
                         role_id=2)

    assert verify_password(password, email_test, db_session)


def test_verify_token():

    token = create_encrypted_token('test@epic-events.com')
    save_token(token, TEST_TOKEN_PATH)

    assert verify_token(TEST_TOKEN_PATH)


def test_load_token():

    assert load_token(TEST_TOKEN_PATH)
