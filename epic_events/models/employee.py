import enum

from sqlalchemy import Column, Integer, String, Enum

from config import Base


class DepartmentType(enum.Enum):
    management = "management"
    commercial = "commercial"
    support = "support"


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    department = Column(Enum(DepartmentType), nullable=False)
