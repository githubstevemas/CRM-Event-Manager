from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from config.config import Base


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey('contract.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    event_date_start = Column(DateTime, nullable=False)
    event_date_end = Column(DateTime, nullable=False)
    support_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    location = Column(String(255))
    attendees = Column(Integer, nullable=False)
    notes = Column(String(255), nullable=False)

    contract = relationship('Contract', back_populates='events')
    client = relationship('Client', back_populates='events')
    support = relationship('Employee', back_populates='events')
