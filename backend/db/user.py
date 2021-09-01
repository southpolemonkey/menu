# User collection
from backend.utilities import get_logger
from .database import Collection
from backend.routers.user import manager

logger = get_logger(__name__)

class UserCollection(Collection):
    def __init__(self):
        self.data = [
            {"id":1, "username":"admin@menuapp.com", "password":"example"},
            {"id":2, "username":"rong@menuapp.com", "password":"doyoulikemeat"},
        ]

user_collection = UserCollection()

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

@manager.user_loader
def find_user(id: str):
    if user := user_collection.find_one({"id": int(id)}):
        return user

def delete_user(id: str):
    pass



