from sqlalchemy.orm import Session
from src.models import EventModel
from src.schemas import Event

# CREATE
def create_event(db: Session, event: Event):

    db_event = EventModel(
        name=event.name,
        location=event.location,
        duration_hours=event.duration_hours
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event

# GET ALL
def get_events(db: Session):
    return db.query(EventModel).all()

# GET BY ID
def get_event(db: Session, event_id: int):
    return db.query(EventModel).filter(EventModel.id == event_id).first()

# DELETE
def delete_event(db: Session, event_id: int):

    event = get_event(db, event_id)

    if event:
        db.delete(event)
        db.commit()

    return event
from src.models import UserModel
from src.auth import hash_password

# ============================================
# USERS
# ============================================

def create_user(
    db: Session,
    username: str,
    password: str
):

    user = UserModel(
        username=username,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user(
    db: Session,
    username: str
):

    return db.query(UserModel).filter(
        UserModel.username == username
    ).first()