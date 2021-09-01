from typing import List

from backend.utilities import get_logger
from .database import Collection

logger = get_logger(__name__)


class MenuCollection(Collection):
    
    def __init__(self):
        self.data = [
            {"id": 1, "name": "红烧肉", "owner": "user@example.com.au", "type": ["Lunch"],
             "ingredients": [{"name": "五花肉", "measurement": "500", "units": "g"}]},
            {"id": 2, "name": "肉末炖蛋", "owner": "user@example.com.au", "type": ["Dinner"],
             "ingredients": [{"name": "猪肉糜", "measurement": "500", "units": "g"}]},
            {"id": 3, "name": "富贵虾", "owner": "user@example.com.au", "type": ["Dinner"],
             "ingredients": [{"name": "大虾", "measurement": "500", "units": "g"}]},
        ]


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


def update_menu(id: str, data: dict):
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
