import os
from pymongo import MongoClient
import uuid

mongo_url = os.getenv('MONGO_URL')
client = MongoClient(mongo_url)
db = client['portfolio']
collection = db['sites']

# Пример тестовых данных
test_data = [
    {
        "id": str(uuid.uuid4()),
        "title": "Site1",
        "url": "http://example.com",
        "description": "Short description",
        "detailed_description": "Detailed description",
        "avatar": "http://example.com/avatar.jpg",
        "screenshots": [
            "http://example.com/screen1.jpg",
            "http://example.com/screen2.jpg",
            "http://example.com/screen3.jpg"
        ]
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Another Site",
        "url": "http://anothersite.com",
        "description": "Another short description",
        "detailed_description": "Another detailed description",
        "avatar": "http://anothersite.com/avatar.jpg",
        "screenshots": [
            "http://anothersite.com/screen1.jpg",
            "http://anothersite.com/screen2.jpg",
            "http://anothersite.com/screen3.jpg"
        ]
    }
]

# Вставка тестовых данных в коллекцию
collection.insert_many(test_data)
