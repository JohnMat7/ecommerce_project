from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    mobile_number = Column(String, unique=True, index=True)
    email_verified = Column(Boolean, default=False)
    mobile_number_verified = Column(Boolean, default=False)
    hashed_password = Column(String)
