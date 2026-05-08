from sqlalchemy import Column, Integer, String
from src.database import Base

# ============================================
# EVENT MODEL
# ============================================

class EventModel(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    duration_hours = Column(Integer, nullable=False)

# ============================================
# USER MODEL
# ============================================

class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)