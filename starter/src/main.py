from fastapi import FastAPI, HTTPException
from src.schemas import Event
from src.models import events

app = FastAPI(
    title="DJ Sound & Lights API",
    description="CRUD de eventos para DJ y sonido",
    version="2.0.0"
)

# ============================================
# ROOT
# ============================================

@app.get("/")
async def root():
    return {
        "message": "DJ Sound & Lights API - Week 02"
    }

# ============================================
# GET ALL EVENTS
# ============================================

@app.get("/events")
async def get_events():
    return events

# ============================================
# GET EVENT BY ID
# ============================================

@app.get("/events/{event_id}")
async def get_event(event_id: int):

    for event in events:
        if event["id"] == event_id:
            return event

    raise HTTPException(status_code=404, detail="Evento no encontrado")

# ============================================
# CREATE EVENT
# ============================================

@app.post("/events")
async def create_event(event: Event):

    events.append(event.dict())

    return {
        "message": "Evento creado correctamente",
        "event": event
    }

# ============================================
# UPDATE EVENT
# ============================================

@app.put("/events/{event_id}")
async def update_event(event_id: int, updated_event: Event):

    for index, event in enumerate(events):

        if event["id"] == event_id:
            events[index] = updated_event.dict()

            return {
                "message": "Evento actualizado",
                "event": updated_event
            }

    raise HTTPException(status_code=404, detail="Evento no encontrado")

# ============================================
# DELETE EVENT
# ============================================

@app.delete("/events/{event_id}")
async def delete_event(event_id: int):

    for index, event in enumerate(events):

        if event["id"] == event_id:
            deleted = events.pop(index)

            return {
                "message": "Evento eliminado",
                "event": deleted
            }

    raise HTTPException(status_code=404, detail="Evento no encontrado")

# ============================================
# HEALTH CHECK
# ============================================

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }