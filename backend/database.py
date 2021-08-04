import motor.motor_asyncio
from bson.objectid import ObjectId
from typing import List

from .utilities import get_logger

logger = get_logger(__name__)

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.menu

# menu_collection = database.get_collection("<collection>")

# A class mimic mongodb collection
class Collection:
    def __init__(self):
        self.data = [
            {"id":1, "name":"红烧肉", "owner":"user@example.com.au","type":["Lunch"],"ingredients":[{"name":"五花肉","measurement":"500","units":"g"}]},
            {"id":2, "name":"肉末炖蛋", "owner":"user@example.com.au","type":["Dinner"],"ingredients":[{"name":"猪肉糜","measurement":"500","units":"g"}]}
        ]

    def insert_one(self, data:dict):
        self.data.append(data)

    def find_all(self):
        return self.data

    def find_one(self, search:dict) -> dict:
        for k,v in search.items():
            for data in self.data:
                if data.get(k) == v:
                    return data
        return

    def delete_one(self, search:dict) -> dict:
        pass

    def update_one(self, search:dict, data:dict):
        if entry := self.find_one(search):
            for k,v in data.items():
                entry[k].update(v)
            return True
        return False


menu_collection = Collection()

def add_menu(menu_data: dict) -> dict:
    logger.info("create new menu")
    menu_collection.insert_one(menu_data)
    return menu_data

def find_menu(id: int) -> dict:
    logger.info("retrieve menu")
    entry = menu_collection.find_one({"id": int(id)})
    return entry

def all_menu() -> List[dict]:
    logger.info("retrieve all menu")
    return menu_collection.find_all()

def delete_menu(id: str):
    logger.info(f"remove menu {id}")
    if menu := menu_collection.find_one({"id": 1}):
        return True

def update_menu(id: str, data:dict):
    if len(data) < 1:
        return False
    menu = menu_collection.find_one({"id": id})
    if menu:
        updated_menu = menu_collection.update_one(
            {"id", id}, {"$set": data}
        )
        if updated_menu:
            return True
        return False

# User collection
def add_user(data: dict):
    pass

def update_user(id: str, data: dict):
    pass