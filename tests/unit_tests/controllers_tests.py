from sqlalchemy import inspect

from epic_events.controllers.authentication import is_email_exists


def test_db_connection(engine):
    inspector = inspect(engine)
    assert inspector.engine.url.database == "test_epic_events"


"""def test_register_employee(db):
    password_test = "qwertyui"

    register("john",
             "doe",
             password_test,
             "test@epic-events.com",
             "+33531313131",
             "1",
             db)

    assert db.query(Employee).filter_by(
        email='test@epic-events.com').first() is not None"""


def test_is_email_exists():
    email_test = "mas.ste"
    assert is_email_exists(email_test)
