from typing import List
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from models import WorkExperience
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']
collection = db['work_experience']

router = APIRouter()

@router.post("/", response_model=WorkExperience)
def create_work_experience(experience: WorkExperience):
    result = collection.insert_one(experience.dict())
    return experience

@router.get("/", response_model=List[WorkExperience])
def get_work_experiences():
    return list(collection.find())

@router.get("/{experience_id}", response_model=WorkExperience)
def get_work_experience(experience_id: str):
    experience = collection.find_one({"_id": experience_id})
    if experience is None:
        raise HTTPException(status_code=404, detail="Work experience not found")
    return experience
