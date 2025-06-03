from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Mood(Base):
    __tablename__ = 'moods'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    mood_type = Column(String(50), nullable=False)  # e.g., "Happy", "Sad", etc.
    journal_entry = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship
    user = relationship("User", backref="moods")

    def __repr__(self):
        return f"<Mood(user_id={self.user_id}, mood_type='{self.mood_type}', timestamp='{self.timestamp}')>"
