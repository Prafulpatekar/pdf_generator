from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class UserBase(BaseModel):
    name: str
    date: str
    address: str
    check_box_activities: Optional[List[str]] = []
    radio_activities: Optional[str] = None


class UserCreate(BaseModel):
    name: str
    date: date
    address: str
    check_box_activities: Optional[List[str]] = []
    radio_activities: Optional[str] = None


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True

radio_options = {
    "reading": 0,
    "walking": 1,
    "music": 2
}