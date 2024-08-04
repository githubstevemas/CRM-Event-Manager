from sqlalchemy import inspect, text

from epic_events.controllers.auth_controller import (is_email_exists,
                                                     register,
                                                     hash_password)
from epic_events.models.employee import Employee
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

    register(test_employee, db_session)

    assert db_session.query(Employee).filter_by(
        email='test@epic-events.com').first() is not None


def test_is_email_exists(db_session, test_engine):
    email_test = "test@exemple.com"

    # Insert new employee
    db_session.execute(
        text(
            "INSERT INTO employee ("
            "email, "
            "password, "
            "first_name, "
            "last_name, "
            "phone, "
            "role_id) "
            "VALUES ("
            ":email, "
            ":password, "
            ":first_name, "
            ":last_name, "
            ":phone, "
            ":role_id)"),
        {"email": email_test, "password": "hashed_password",
         "first_name": "Test", "last_name": "User", "phone": "1234567890",
         "role_id": "2"}
    )
    db_session.commit()

    assert is_email_exists(email_test, db_session)
