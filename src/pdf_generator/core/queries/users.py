from sqlalchemy.orm import Session
from pdf_generator.models.users import User
from pdf_generator.schemas.users import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        date=user.date,
        address=user.address,
        check_box_activities=user.check_box_activities,
        raido_activities= user.radio_activities
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user