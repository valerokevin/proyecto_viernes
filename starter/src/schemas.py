from pydantic import BaseModel

# ============================================
# EVENT SCHEMAS
# ============================================

class Event(BaseModel):
    name: str
    location: str
    duration_hours: int

class EventResponse(Event):
    id: int

    class Config:
        from_attributes = True

# ============================================
# USER SCHEMAS
# ============================================

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str