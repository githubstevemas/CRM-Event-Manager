from sqlalchemy import Column, Integer, String

from config import Base


class Employee(Base):
    __tablename__ = 'employee'

    id = Column("id", Integer, primary_key=True)
    password = Column("password", String)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    email = Column("email", String)
    phone = Column("phone", Integer)
    department = Column("department", String)
