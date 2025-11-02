from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class ItemCreate(BaseModel):
    title: str
    description: str
    location: str
    type: str
    email: str

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    type: Optional[str] = None
    email: Optional[str] = None

class ItemResponse(BaseModel):
    id: UUID
    user_id: UUID
    type: str
    title: str
    description: str
    location: str
    image_url: Optional[str]
    status: Optional[str]  # allow None
    email: str
    created_at: datetime
