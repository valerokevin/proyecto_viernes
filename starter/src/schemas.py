from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name: str
    location: str
    duration_hours: int