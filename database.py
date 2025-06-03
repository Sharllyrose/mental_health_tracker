from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
try:
    from .models import Base
except ImportError:
    from models import Base

# Create database engine
DATABASE_URL = "sqlite:///mental_health.db"
engine = create_engine(DATABASE_URL)

# Create session factory
Session = sessionmaker(bind=engine)

def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(engine)

def get_session():
    """Get a new database session."""
    return Session()
