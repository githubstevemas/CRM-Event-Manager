from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.config import Base


class EmployeeRole(Base):
    __tablename__ = 'employee_role'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    employees = relationship('Employee', back_populates='role')


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    role_id = Column(Integer, ForeignKey('employee_role.id'), nullable=False)

    role = relationship('EmployeeRole', back_populates='employees')
