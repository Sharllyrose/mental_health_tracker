from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String(50), nullable=False)  # e.g., "Meditation", "Exercise"
    duration_minutes = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship
    user = relationship("User", backref="activities")

    def __repr__(self):
        return f"<Activity(user_id={self.user_id}, activity_type='{self.activity_type}', duration={self.duration_minutes}min)>"
