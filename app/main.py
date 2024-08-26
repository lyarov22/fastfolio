from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любого домена. Замените на список разрешенных доменов.
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Разрешает все HTTP методы
    allow_headers=["*"],  # Разрешает все заголовки
)

# Routers
from routers import sites, achievements, figma_projects, work_experience, other

app.include_router(sites.router, prefix='/sites', tags=['sites'])
app.include_router(achievements.router, prefix='/achievements', tags=['achievements'])
app.include_router(figma_projects.router, prefix='/figma_projects', tags=['figma_projects'])
app.include_router(work_experience.router, prefix='/work_experience', tags=['work_experience'])
app.include_router(other.router, prefix='/other', tags=['other'])
