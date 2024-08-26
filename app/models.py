from pydantic import BaseModel
from typing import List, Optional

from pydantic import BaseModel
from typing import List
import uuid

class Site(BaseModel):
    id: str  # Используем строку для UUID
    title: str
    url: str
    description: Optional[str] = None
    detailed_description: str
    avatar: str
    screenshots: List[str]
    per: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": str(uuid.uuid4()),  # Пример UUID
                "title": "Example Site",
                "url": "http://example.com",
                "description": "A short description",
                "detailed_description": "A detailed description",
                "avatar": "http://example.com/avatar.jpg",
                "screenshots": [
                    "http://example.com/screen1.jpg",
                    "http://example.com/screen2.jpg",
                    "http://example.com/screen3.jpg"
                ]
            }
        }

class Achievement(BaseModel):
    title: str
    date: str
    photo: str
    per: int

class FigmaProject(BaseModel):
    title: str
    description: Optional[str] = None
    url: str
    avatar: str
    per: int

class WorkExperience(BaseModel):
    title: str
    start_date: str
    end_date: str
    duration: str
    company: str
    responsibilities: List[str]
    per: int

class Other(BaseModel):
    title: str
    description: Optional[str] = None
    url: Optional[str] = None
    avatar: str
    per: int