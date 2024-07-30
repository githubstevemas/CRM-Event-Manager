from sqlalchemy import inspect

from epic_events.controllers.authentication import register, is_email_exists


def test_db_connection(engine):

    inspector = inspect(engine)
    assert inspector.engine.url.database == "test_epic_events"


def test_register_employee(db):

    password_test = "qwertyui"

    register_test = register("john",
                             "doe",
                             password_test,
                             "test@epic-events.com",
                             "+33531313131",
                             "3",
                             db)

    assert register_test.first_name == "john"
    assert register_test.password != password_test


def test_is_email_exists():

    email_test = "mas.ste"
    assert is_email_exists(email_test)
