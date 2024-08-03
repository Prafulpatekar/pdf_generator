from sqlalchemy import Column, Integer, String, Date, JSON
from pdf_generator.core.utils.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=50))
    date = Column(Date)
    address = Column(String(length=200))
    check_box_activities = Column(JSON)
    raido_activities = Column(String(length=30))
    