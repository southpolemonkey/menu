from typing import Optional, List
from pydantic import BaseModel, Field

from enum import Enum

class MenuType(Enum):
    Lunch = 1
    Breakfast = 2
    Dinner = 3

class Ingredient:
    name: str = Field(...)
    measurement: str = Field(...)
    units: str = Optional[str]

class MenuSchema(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    owner: str
    followers: Optional[List[str]]
    type: Optional[List[str]]
    ingredients: List[Ingredient]
    createAt: str
    updateAt: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "红烧狮子头",
                "owner": "user@example.com",
                "type": ["Dinner"],
                "ingredients": [{"name":"猪肉", "measurement":"600", "units":"g"}],
                "createAt": "2021-08-03 16:41:48.847402",
                "updateAt": "2021-08-03 16:41:48.847402",
            }
        }

class UpdateMenuSchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    owner: Optional[str]
    followers: Optional[str]
    type: Optional[List[str]]
    ingredients: Optional[List[Ingredient]]
    updateAt: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "红烧狮子头",
                "owner": "user@example.com",
                "type": ["Dinner"],
                "ingredients": [{"name":"猪肉", "measurement":"800", "units":"g"}],
                "updateAt": "2021-08-03 22:14:00.00000",
            }
        }