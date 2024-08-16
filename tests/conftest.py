import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config.config import TEST_DATABASE_URL, Base
from epic_events.controllers.auth_controller import hash_password


@pytest.fixture(scope="session")
def test_engine():
    test_engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(test_engine)
    yield test_engine
    Base.metadata.drop_all(test_engine)


@pytest.fixture(scope="session")
def TestSessionFactory(test_engine):
    TestSessionLocal = sessionmaker(bind=test_engine)
    yield TestSessionLocal


@pytest.fixture()
def db_session(TestSessionFactory):
    db_session = TestSessionFactory()
    yield db_session
    db_session.close()


@pytest.fixture(autouse=True)
def override_global_db_session(db_session):
    global global_db_session
    global_db_session = db_session


@pytest.fixture()
def insert_test_employee(db_session):
    def insert(email, password, first_name, last_name, phone, role_id):
        hashed_password = hash_password(password)
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
            {"email": email, "password": hashed_password,
             "first_name": first_name, "last_name": last_name,
             "phone": phone, "role_id": role_id}
        )
        db_session.commit()

    return insert


@pytest.fixture()
def insert_test_client(db_session):
    def insert(first_name, last_name, email, phone, company_name,
               first_contact, commercial_id):
        db_session.execute(
            text(
                "INSERT INTO client ("
                "first_name, "
                "last_name, "
                "email, "
                "phone, "
                "company_name, "
                "first_contact, "
                "commercial_id) "
                "VALUES ("
                ":first_name, "
                ":last_name, "
                ":email, "
                ":phone, "
                ":company_name, "
                ":first_contact, "
                ":commercial_id)"),
            {"first_name": first_name, "last_name": last_name,
             "email": email, "phone": phone, "company_name": company_name,
             "first_contact": first_contact, "commercial_id": commercial_id}
        )
        db_session.commit()

    return insert


def insert_roles_in_table(db_session):

    db_session.execute(
        text("INSERT INTO employee_role (id, name) VALUES (:id, :name)"),
        [{"id": 1, "name": "commercial"},
         {"id": 2, "name": "support"},
         {"id": 3, "name": "management"}]
    )
    db_session.commit()
