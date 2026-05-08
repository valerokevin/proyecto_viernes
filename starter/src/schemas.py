from pydantic import BaseModel

class Event(BaseModel):
    name: str
    location: str
    duration_hours: int

class EventResponse(Event):
    id: int

    class Config:
        from_attributes = True