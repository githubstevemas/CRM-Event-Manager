from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from config.config import Base


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    company_name = Column(String(100), nullable=False)
    first_contact = Column(DateTime, default=datetime.now())
    last_update = Column(DateTime)
    commercial_id = Column(Integer, ForeignKey('employee.id'), nullable=False)

    commercial = relationship('Employee', back_populates='clients')
