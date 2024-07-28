from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'

    id = Column("id", Integer, primary_key=True)
    password = Column("password", String)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    email = Column("email", String)
    phone = Column("phone", Integer)
    company_name = Column("company_name", String)
    first_contact_date = Column(
        "first_contact_date",
        DateTime,
        default=datetime.now()
    )
    last_update = Column("last_update", DateTime)
    commercial_id = Column("commercial_id", String)
