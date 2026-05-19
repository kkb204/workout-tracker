from sqlalchemy import Column, Integer, String
from app.database import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    duration = Column(Integer)
    date = Column(String)