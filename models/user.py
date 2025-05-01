from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)  
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)

    symptoms = relationship("Symptom", back_populates="user")