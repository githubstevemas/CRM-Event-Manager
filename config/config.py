import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# Get ids from .env file
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USERNAME = os.getenv('DB_USERNAME')

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'epic_events'

TEST_DB = 'test_epic_events'

# Configure en create database engine
DATABASE_URL = \
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TEST_DATABASE_URL = \
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{TEST_DB}"

# Disable SQL logging
main_engine = create_engine(DATABASE_URL, echo=False)

# Get tables and create session
Base = declarative_base()
SessionFactory = sessionmaker(bind=main_engine)
global_db_session = SessionFactory()
