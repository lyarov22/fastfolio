from typing import List
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from models import Other
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']
collection = db['other']

router = APIRouter()

@router.post("/", response_model=Other)
def create_other_project(project: Other):
    result = collection.insert_one(project.dict())
    return project

@router.get("/", response_model=List[Other])
def get_other_projects():
    return list(collection.find())

@router.get("/{project_id}", response_model=Other)
def get_other_project(project_id: str):
    project = collection.find_one({"_id": project_id})
    if project is None:
        raise HTTPException(status_code=404, detail="Other project not found")
    return project
