import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config.config import TEST_DATABASE_URL, Base


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


def insert_roles_in_table(db_session):
    # Insert roles
    db_session.execute(
        text("INSERT INTO employee_role (id, name) VALUES (:id, :name)"),
        [{"id": 1, "name": "commercial"},
         {"id": 2, "name": "support"},
         {"id": 3, "name": "management"}]
    )
    db_session.commit()
