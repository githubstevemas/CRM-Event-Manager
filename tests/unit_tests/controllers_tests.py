from sqlalchemy import inspect

from epic_events.controllers.authentication import register


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
                             "management",
                             db)

    assert register_test.first_name == "john"
    assert register_test.password != password_test
