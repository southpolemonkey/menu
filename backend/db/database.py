from abc import ABC
import motor.motor_asyncio
from bson.objectid import ObjectId
from typing import List

from backend.utilities import get_logger

from backend.routers.user import manager

logger = get_logger(__name__)

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.menu

# menu_collection = database.get_collection("<collection>")

class Collection:
    def __init__(self):
        self.data = None

    def insert_one(self, data:dict):
        self.data.append(data)

    def find_all(self):
        return self.data

    def find_one(self, search:dict) -> dict:
        for k,v in search.items():
            for data in self.data:
                if data.get(k) == v:
                    return data

    def delete_one(self, search:dict) -> dict:
        pass

    def update_one(self, search:dict, data:dict):
        if entry := self.find_one(search):
            for k,v in data.items():
                entry[k].update(v)
            return True
        return False






