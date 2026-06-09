from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from app.core.config import encrypt_data, decrypt_data

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True) # Nullable for Google Auth users
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="student") # admin, teacher, student
    google_id = Column(String, unique=True, index=True, nullable=True)
    
    # Encrypted fields for "Level 17" security
    _address = Column("address", Text, nullable=True)
    _phone_number = Column("phone_number", String, nullable=True)

    @property
    def address(self):
        return decrypt_data(self._address) if self._address else None

    @address.setter
    def address(self, value):
        self._address = encrypt_data(value) if value else None

    @property
    def phone_number(self):
        return decrypt_data(self._phone_number) if self._phone_number else None

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = encrypt_data(value) if value else None

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    subject = Column(String, index=True)
    score = Column(Integer) # For C++ analytics
    max_score = Column(Integer)
    date_recorded = Column(DateTime, default=datetime.datetime.utcnow)

    student = relationship("User")
