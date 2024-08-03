# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pdf_generator.configs.settings import POSTGRES_URL

# Get the database URL from environment variables or set a default
# DATABASE_URL = os.getenv("DATABASE_URL", POSTGRES_URL)
DATABASE_URL = "sqlite:///./pdf_generator.db"

 
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

# Create tables if they don't exist
def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        