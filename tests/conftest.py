import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import TEST_DATABASE_URL, Base


@pytest.fixture()
def engine():
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture()
def Session(engine):
    SessionLocal = sessionmaker(bind=engine)
    yield SessionLocal


@pytest.fixture()
def db(Session):
    session = Session()
    yield session
    session.close()
