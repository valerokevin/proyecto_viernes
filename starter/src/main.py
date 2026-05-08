from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import SessionLocal, engine
from src.models import Base
from src.schemas import Event, EventResponse
from src.crud import (
    create_event,
    get_events,
    get_event,
    delete_event
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DJ Sound & Lights API",
    version="3.0.0"
)

# ============================================
# DATABASE DEPENDENCY
# ============================================

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# ============================================
# ROOT
# ============================================

@app.get("/")
async def root():
    return {
        "message": "DJ Sound & Lights API - Week 03"
    }

# ============================================
# CREATE EVENT
# ============================================

@app.post("/events", response_model=EventResponse)
def create_new_event(
    event: Event,
    db: Session = Depends(get_db)
):

    return create_event(db, event)

# ============================================
# GET EVENTS
# ============================================

@app.get("/events", response_model=list[EventResponse])
def read_events(db: Session = Depends(get_db)):

    return get_events(db)

# ============================================
# GET EVENT BY ID
# ============================================

@app.get("/events/{event_id}", response_model=EventResponse)
def read_event(
    event_id: int,
    db: Session = Depends(get_db)
):

    event = get_event(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Evento no encontrado"
        )

    return event

# ============================================
# DELETE EVENT
# ============================================

@app.delete("/events/{event_id}")
def remove_event(
    event_id: int,
    db: Session = Depends(get_db)
):

    event = delete_event(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Evento no encontrado"
        )

    return {
        "message": "Evento eliminado"
    }

# ============================================
# HEALTH
# ============================================

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }