import enum
from typing import Optional, List

from pydantic import BaseModel, Field

from .menu import MenuSchema

class Day(enum.Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

class Plan:
    day: Day
    breakfast: List[MenuSchema]
    lunch: List[MenuSchema]
    dinner: List[MenuSchema]

# TODO: CHECK IF FASTAPI HAS DATETIME TYPE
class WeeklyPlanSchema(BaseModel):
    id: str
    owner: str
    numGuests: int
    planStartDate: str
    planEndDate: str
    createAt: str
    updateAt: str
    plans: List[Plan]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
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

        }

class PartyPlanSchema(BaseModel):
    id: str
    owner: str
    numGuests: int
    planStartDate: str
    occasion: Optional[str]
    createAt: str
    updateAt: str
    plans: List[Plan]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": "b11b9e65-0e57-4c92-882f-616b584c835a",
                "owner": "username@example.com.au",
                "numGuests": 4,
                "planStartDate": "2021-08-02",
                "occasion": "中秋节",
                "createAt": "2021-08-03 16:41:48.847402",
                "updateAt": "2021-08-03 16:41:48.847402",
                "plans": []
            }
        }

