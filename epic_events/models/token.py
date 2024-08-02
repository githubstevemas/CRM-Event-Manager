from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import Base


class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    token = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee", back_populates="token")
