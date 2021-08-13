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
            {"id":2, "name":"肉末炖蛋", "owner":"user@example.com.au","type":["Dinner"],"ingredients":[{"name":"猪肉糜","measurement":"500","units":"g"}]},
            {"id":3, "name":"富贵虾", "owner":"user@example.com.au","type":["Dinner"],"ingredients":[{"name":"大虾","measurement":"500","units":"g"}]},
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

class UserCollection(Collection):
    def __init__(self):
        self.data = [
            {"id":1, "username":"admin@menuapp.com", "password":"example"},
            {"id":2, "username":"rong@menuapp.com", "password":"doyoulikemeat"},
        ]

class PlanCollection(Collection):
    def __init__(self):
        self.data = [
            {
                "id": "b11b9e65-0e57-4c92-882f-616b584c835a",
                "owner": "username@example.com.au",
                "numGuests": 3,
                "planStartDate": "2021-08-02",
                "planEndDate": "2021-08-08",
                "createAt": "2021-08-03 16:41:48.847402",
                "updateAt": "2021-08-03 16:41:48.847402",
                "plans": [
                    {
                        "day": "MON",
                        "breakfast": [
                            {
                                "id": 1,
                                "name": "牛奶麦片",
                                "owner": "user@example.com",
                                "type": ["breakfast"],
                                "ingredients": [
                                    {"name": "牛奶", "measurement": "200", "units": "ml"},
                                    {"name": "燕麦片", "measurement": "50g", "units": "g"}
                                ],
                                "createAt": "2021-08-03 16:41:48.847402",
                                "updateAt": "2021-08-03 16:41:48.847402",
                            }
                        ],
                        "lunch": [
                            {
                                "id": 2,
                                "name": "鸡肉卷",
                                "owner": "user@example.com",
                                "type": ["lunch", "breakfast"],
                                "ingredients": [
                                    {"name": "鸡肉", "measurement": "400", "units": "g"},
                                    {"name": "生菜", "measurement": "30", "units": "g"},
                                    {"name": "青椒", "measurement": "50", "units": "g"},
                                    {"name": "卷饼", "measurement": "2", "units": "pieces"},
                                ],
                                "createAt": "2021-08-03 16:41:48.847402",
                                "updateAt": "2021-08-03 16:41:48.847402",
                            }
                        ],
                        "dinner": [
                            {
                                "id": 3,
                                "name": "清蒸带鱼",
                                "owner": "user@example.com",
                                "type": ["dinner"],
                                "ingredients": [
                                    {"name": "带鱼", "measurement": "500", "units": "g"},
                                    {"name": "葱姜", "measurement": "20", "units": "g"},
                                ],
                                "createAt": "2021-08-03 16:41:48.847402",
                                "updateAt": "2021-08-03 16:41:48.847402",
                            }
                        ]
                    }
                ]
            }
        ]


menu_collection = Collection()
user_collection = UserCollection()
plan_collection = PlanCollection()

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
# TODO: Implement user CRUD methods
def add_user(data: dict):
    logger.info("Create new user")
    entry = user_collection.insert_one(data)
    return entry

def update_user(id: str, data: dict):
    logger.info("Update user info")
    if len(data) < 1:
        return False
    user = user_collection.find_one({"id": int(id)})
    if user:
        updated_user = user_collection.update_one(
            {"id": id, "$set": data}
        )
        if updated_user:
            return True
        return False

def find_user(id: str):
    if user := user_collection.find_one({"id": int(id)}):
        return user

def delete_user(id: str):
    pass


# Plans collection
def add_plan(data: dict):
    pass

def update_plan(id: str, data:dict):
    pass

def delete_plan(id: str):
    pass
