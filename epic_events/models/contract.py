from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import relationship

from config.config import Base


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    commercial_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    amount = Column(Numeric, nullable=False)
    left_to_pay = Column(Numeric, nullable=False)
    contract_creation_date = Column(DateTime, default=datetime.now)
    status = Column(Boolean, default=False)

    client = relationship('Client', back_populates='contracts')
    commercial = relationship('Employee', back_populates='contracts')
    events = relationship('Event', back_populates='contract')
