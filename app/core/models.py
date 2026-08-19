from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func 
from app.core.database import base 

class User(base):
    __tablename__ = "user"

    id=Column(Integer, primary_key=True, auto_increment=True)
    email=Column(String, unique=True, nullable=False)
    emp_id=Column(Integer, unique=True,nullable=False)
    username=Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    invoices = relationship(
        "invoice",
        back_populates="userid"
    )
