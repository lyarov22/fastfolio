from typing import List
from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from models import FigmaProject
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']
collection = db['figma_projects']

router = APIRouter()

@router.post("/", response_model=FigmaProject)
def create_figma_project(project: FigmaProject):
    result = collection.insert_one(project.dict())
    return project

@router.get("/", response_model=List[FigmaProject])
def get_figma_projects():
    return list(collection.find())

@router.get("/{project_id}", response_model=FigmaProject)
def get_figma_project(project_id: str):
    project = collection.find_one({"_id": project_id})
    if project is None:
        raise HTTPException(status_code=404, detail="Figma project not found")
    return project
