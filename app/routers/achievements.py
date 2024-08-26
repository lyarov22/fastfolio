from typing import List
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from models import Achievement
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']
collection = db['achievements']

router = APIRouter()

@router.post("/", response_model=Achievement)
def create_achievement(achievement: Achievement):
    result = collection.insert_one(achievement.dict())
    return achievement

@router.get("/", response_model=List[Achievement])
def get_achievements():
    return list(collection.find())

@router.get("/{achievement_id}", response_model=Achievement)
def get_achievement(achievement_id: str):
    achievement = collection.find_one({"_id": achievement_id})
    if achievement is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return achievement
