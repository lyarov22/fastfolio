from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from models import Site
from typing import Dict, List
import os
from dotenv import load_dotenv
import uuid

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']
collection = db['sites']

router = APIRouter()

@router.get("/", response_model=List[Site])
def get_sites():
    return list(collection.find())

@router.post("/", response_model=Site)
def create_site(site: Site):
    site_id = str(uuid.uuid4())  # Генерация нового UUID
    site_dict = site.dict()
    site_dict['id'] = site_id
    collection.insert_one(site_dict)
    return site_dict

@router.get("/{site_id}", response_model=Site)
def get_site(site_id: str):
    site = collection.find_one({"id": site_id})
    if site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.put("/{site_id}", response_model=Site)
def update_site(site_id: str, site: Site):
    result = collection.update_one({"id": site_id}, {"$set": site.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.delete("/{site_id}", response_model=Dict[str, str])
def delete_site(site_id: str):
    result = collection.delete_one({"id": site_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Site not found")
    return {"detail": "Site deleted"}
